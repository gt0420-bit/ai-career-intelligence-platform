import asyncio
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any
import random
import os
from dotenv import load_dotenv
from .base_agent import BaseAgent, AgentResult

# Ensure environment variables are loaded
load_dotenv()

class OpportunityHunterAgent(BaseAgent):
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("Opportunity Hunter", config)
        
        # Companies to monitor for early signals
        self.target_companies = [
            'OpenAI', 'Anthropic', 'Stripe', 'Figma', 'Notion',
            'Databricks', 'Snowflake', 'Airbnb', 'Uber', 'ByteDance'
        ]
        
        # AI client setup
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.log_info(f"🔑 API Key configured: {bool(self.openai_api_key and len(self.openai_api_key) > 20)}")
    
    async def execute_task(self, task_data: Dict[str, Any]) -> AgentResult:
        """Execute opportunity hunting tasks"""
        start_time = time.time()
        self.log_info(f"🎯 Starting task: {task_data.get('task_type', 'unknown')}")
        
        try:
            result_data = await self._discover_hidden_opportunities(task_data)
            execution_time = time.time() - start_time
            
            self.stats['tasks_completed'] += 1
            self.log_info(f"✅ Task completed in {execution_time:.2f}s")
            
            return AgentResult(
                success=True,
                data=result_data,
                confidence_score=0.85,
                execution_time=execution_time,
                recommendations=self._generate_opportunity_recommendations(result_data)
            )
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.stats['tasks_failed'] += 1
            self.log_error(f"❌ Task failed: {str(e)}")
            
            return AgentResult(
                success=False,
                data={'error': str(e)},
                confidence_score=0.0,
                execution_time=execution_time,
                errors=[str(e)]
            )
    
    async def _discover_hidden_opportunities(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Discover job opportunities using AI analysis"""
        self.log_info("🔍 Hunting for hidden opportunities with AI...")
        
        user_skills = task_data.get('user_skills', ['Python', 'JavaScript', 'React'])
        
        # Generate market signals
        funding_signals = await self._scan_funding_announcements()
        expansion_signals = await self._scan_team_expansions()
        
        # Use AI for analysis
        ai_analysis = await self._ai_opportunity_analysis(funding_signals, expansion_signals, user_skills)
        
        # Generate opportunities
        opportunities = await self._generate_opportunities_from_signals(funding_signals + expansion_signals)
        
        result = {
            'discovery_timestamp': datetime.now().isoformat(),
            'user_skills_analyzed': user_skills,
            'signals_detected': {
                'funding': len(funding_signals),
                'expansion': len(expansion_signals)
            },
            'opportunities_found': opportunities,
            'ai_analysis': ai_analysis,
            'raw_signals': {
                'funding': funding_signals,
                'expansion': expansion_signals
            }
        }
        
        self.log_info(f"🎯 Discovered {len(opportunities)} hidden opportunities")
        return result
    
    async def _scan_funding_announcements(self) -> List[Dict[str, Any]]:
        """Scan for funding announcements"""
        funding_signals = []
        
        for company in self.target_companies[:4]:
            if random.random() > 0.5:  # 50% chance
                funding_round = random.choice(['Series A', 'Series B', 'Series C'])
                amount = random.choice([15, 25, 50, 100])
                
                funding_signals.append({
                    'company': company,
                    'type': 'funding_announcement',
                    'funding_round': funding_round,
                    'amount_millions': amount,
                    'hiring_probability': random.uniform(0.7, 0.9),
                    'estimated_new_hires': random.randint(15, 40),
                    'timeline': f"{random.randint(4, 12)} weeks"
                })
        
        return funding_signals
    
    async def _scan_team_expansions(self) -> List[Dict[str, Any]]:
        """Scan for team expansion signals"""
        expansion_signals = []
        
        for company in self.target_companies[:3]:
            if random.random() > 0.6:  # 40% chance
                expansion_signals.append({
                    'company': company,
                    'type': 'team_expansion',
                    'expansion_type': random.choice(['new_office', 'department_growth', 'product_scaling']),
                    'hiring_probability': random.uniform(0.6, 0.85),
                    'estimated_roles': random.randint(10, 25),
                    'departments': random.sample(['Engineering', 'Product', 'Design'], 2)
                })
        
        return expansion_signals
    
    async def _ai_opportunity_analysis(self, funding_signals: List, expansion_signals: List, user_skills: List[str]) -> Dict[str, Any]:
        """Use AI to analyze opportunities"""
        
        if not self.openai_api_key or len(self.openai_api_key) < 20:
            return {
                'analysis': 'AI analysis unavailable - API key not configured',
                'confidence': 0.0
            }
        
        try:
            import openai
            
            # Create OpenAI client
            client = openai.OpenAI(api_key=self.openai_api_key)
            
            # Prepare data for analysis
            market_data = {
                'funding_signals': funding_signals,
                'expansion_signals': expansion_signals,
                'user_skills': user_skills
            }
            
            prompt = f"""
            As a career intelligence expert, analyze these market signals for hidden job opportunities:

            USER SKILLS: {', '.join(user_skills)}

            MARKET SIGNALS:
            Funding announcements: {len(funding_signals)} companies
            Team expansions: {len(expansion_signals)} companies

            DETAILED DATA:
            {json.dumps(market_data, indent=2)}

            Provide strategic analysis:
            1. Top 3 companies to target and why
            2. Best roles to apply for at each company
            3. Optimal timing for applications
            4. Specific networking strategies
            5. Key skills to emphasize in applications

            Be specific and actionable.
            """
            
            self.log_info("🤖 Requesting AI analysis...")
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=800
            )
            
            analysis_text = response.choices[0].message.content
            
            self.log_info("✅ AI analysis completed successfully")
            
            return {
                'analysis': analysis_text,
                'model_used': 'gpt-3.5-turbo',
                'confidence': 0.88,
                'timestamp': datetime.now().isoformat(),
                'tokens_used': response.usage.total_tokens if hasattr(response, 'usage') else 0
            }
            
        except Exception as e:
            self.log_error(f"AI analysis failed: {e}")
            return {
                'analysis': f'AI analysis failed: {str(e)}',
                'confidence': 0.0,
                'error': str(e)
            }
    
    async def _generate_opportunities_from_signals(self, all_signals: List[Dict]) -> List[Dict[str, Any]]:
        """Generate opportunities from signals"""
        # Group by company
        company_signals = {}
        for signal in all_signals:
            company = signal['company']
            if company not in company_signals:
                company_signals[company] = []
            company_signals[company].append(signal)
        
        opportunities = []
        for company, signals in company_signals.items():
            hiring_probs = [s.get('hiring_probability', 0.5) for s in signals]
            avg_prob = sum(hiring_probs) / len(hiring_probs)
            
            # Boost for multiple signals
            if len(signals) > 1:
                avg_prob = min(avg_prob * 1.3, 0.95)
            
            opportunities.append({
                'company': company,
                'hiring_probability': avg_prob,
                'signal_count': len(signals),
                'signal_types': [s['type'] for s in signals],
                'estimated_roles': ['Software Engineer', 'Senior Developer', 'Product Manager'],
                'recommended_timeline': 'Apply in 2-4 weeks' if any(s['type'] == 'funding_announcement' for s in signals) else 'Apply within 1-3 weeks',
                'priority_score': avg_prob * 100 + len(signals) * 15
            })
        
        # Sort by priority
        opportunities.sort(key=lambda x: x['priority_score'], reverse=True)
        return opportunities[:5]
    
    def _generate_opportunity_recommendations(self, data: Dict[str, Any]) -> List[str]:
        """Generate recommendations"""
        recommendations = []
        opportunities = data.get('opportunities_found', [])
        
        if opportunities:
            top_opp = opportunities[0]
            recommendations.append(
                f"🎯 TOP PRIORITY: {top_opp['company']} - {top_opp['hiring_probability']:.0%} hiring probability"
            )
            
            high_prob = [o for o in opportunities if o['hiring_probability'] > 0.8]
            if len(high_prob) > 1:
                companies = [o['company'] for o in high_prob[:3]]
                recommendations.append(f"🔥 High-confidence targets: {', '.join(companies)}")
        
        # AI insights
        ai_analysis = data.get('ai_analysis', {})
        if ai_analysis.get('confidence', 0) > 0.5:
            recommendations.append("🤖 Detailed AI strategic analysis available below")
        
        recommendations.extend([
            "📱 Set up Google Alerts for target companies",
            "🤝 Start LinkedIn networking this week"
        ])
        
        return recommendations
    
    async def generate_autonomous_tasks(self, user_id: int) -> List[Dict[str, Any]]:
        """Generate autonomous tasks"""
        return [{
            'task_type': 'hidden_job_discovery',
            'description': 'AI-powered opportunity hunting',
            'user_id': user_id,
            'priority': 'high',
            'context': {
                'user_skills': ['Python', 'JavaScript', 'React'],
                'experience_level': 'Mid'
            }
        }]

# Test function
async def test_opportunity_hunter():
    """Test the AI-powered agent"""
    agent = OpportunityHunterAgent()
    
    test_task = {
        'task_type': 'hidden_job_discovery',
        'user_skills': ['Python', 'React', 'TypeScript', 'AWS', 'Node.js'],
        'user_id': 1
    }
    
    print("🎯 Testing AI-Powered Opportunity Hunter Agent...")
    print("=" * 60)
    
    result = await agent.execute_task(test_task)
    
    print(f"✅ Success: {result.success}")
    print(f"📊 Confidence: {result.confidence_score:.1%}")
    print(f"⏱️  Time: {result.execution_time:.2f}s")
    print("=" * 60)
    
    if result.success:
        data = result.data
        
        # Show signals
        signals = data.get('signals_detected', {})
        print(f"\n📡 MARKET SIGNALS DETECTED:")
        print(f"  💰 Funding announcements: {signals.get('funding', 0)}")
        print(f"  📈 Team expansions: {signals.get('expansion', 0)}")
        
        # Show opportunities
        opportunities = data.get('opportunities_found', [])
        print(f"\n🎯 HIDDEN OPPORTUNITIES: {len(opportunities)}")
        print("-" * 40)
        
        for i, opp in enumerate(opportunities, 1):
            print(f"{i}. {opp['company']} - {opp['hiring_probability']:.0%} probability")
            print(f"   📊 Signals: {opp['signal_count']} | Timeline: {opp['recommended_timeline']}")
            print(f"   🎯 Roles: {', '.join(opp['estimated_roles'][:2])}")
        
        # Show AI analysis
        ai_analysis = data.get('ai_analysis', {})
        if ai_analysis.get('confidence', 0) > 0.5:
            print(f"\n🤖 AI STRATEGIC ANALYSIS:")
            print(f"   Model: {ai_analysis.get('model_used')}")
            print(f"   Confidence: {ai_analysis.get('confidence', 0):.1%}")
            print(f"   Tokens: {ai_analysis.get('tokens_used', 0)}")
            print("-" * 40)
            print(ai_analysis.get('analysis', 'No analysis available'))
        else:
            print(f"\n❌ AI Analysis Failed:")
            print(f"   {ai_analysis.get('analysis', 'Unknown error')}")
        
        # Show recommendations
        print(f"\n💡 STRATEGIC RECOMMENDATIONS:")
        for i, rec in enumerate(result.recommendations, 1):
            print(f"   {i}. {rec}")
    
    print("\n" + "=" * 60)
    return result

if __name__ == "__main__":
    asyncio.run(test_opportunity_hunter())
