import asyncio
import json
import requests
import time  # Added this missing import
from datetime import datetime, timedelta
from typing import Dict, List, Any
import random
from .base_agent import BaseAgent, AgentResult

class MarketScoutAgent(BaseAgent):
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("Market Scout", config)
        
        self.monitored_companies = [
            'Google', 'Microsoft', 'OpenAI', 'Anthropic', 'Meta', 
            'Apple', 'Amazon', 'Netflix', 'Tesla', 'Stripe'
        ]
        
        self.job_sources = ['Indeed', 'LinkedIn', 'Glassdoor']
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
    
    async def execute_task(self, task_data: Dict[str, Any]) -> AgentResult:
        """Execute market intelligence tasks"""
        start_time = time.time()
        self.log_info(f"Starting task: {task_data.get('task_type', 'unknown')}")
        
        try:
            task_type = task_data.get('task_type')
            
            if task_type == "daily_market_scan":
                result_data = await self._daily_market_scan(task_data)
            elif task_type == "company_intelligence":
                result_data = await self._company_intelligence_scan(task_data)
            elif task_type == "skill_demand_analysis":
                result_data = await self._skill_demand_analysis(task_data)
            else:
                raise ValueError(f"Unknown task type: {task_type}")
            
            execution_time = time.time() - start_time
            
            self.stats['tasks_completed'] += 1
            self.log_info(f"Task completed in {execution_time:.2f}s")
            
            return AgentResult(
                success=True,
                data=result_data,
                confidence_score=0.85,
                execution_time=execution_time,
                recommendations=self._generate_recommendations(result_data)
            )
            
        except Exception as e:
            execution_time = time.time() - start_time
            self.stats['tasks_failed'] += 1
            self.log_error(f"Task failed: {str(e)}")
            
            return AgentResult(
                success=False,
                data={'error': str(e)},
                confidence_score=0.0,
                execution_time=execution_time,
                errors=[str(e)]
            )
    
    async def _daily_market_scan(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform daily market intelligence scan"""
        self.log_info("🔍 Performing daily market scan...")
        
        user_skills = task_data.get('user_skills', ['Python', 'JavaScript', 'React'])
        
        # Simulate market scanning (in production, this would scrape real data)
        market_data = {
            'scan_timestamp': datetime.utcnow().isoformat(),
            'job_opportunities': await self._scan_job_opportunities(user_skills),
            'salary_trends': await self._analyze_salary_trends(user_skills),
            'company_activity': await self._scan_company_activity(),
            'skill_trends': await self._analyze_skill_trends(user_skills),
            'market_summary': {}
        }
        
        # Generate market summary
        total_jobs = sum(opp['job_count'] for opp in market_data['job_opportunities'])
        market_data['market_summary'] = {
            'total_opportunities': total_jobs,
            'market_heat': 'Hot' if total_jobs > 500 else 'Warm' if total_jobs > 200 else 'Cool',
            'top_skills_in_demand': [skill['name'] for skill in market_data['skill_trends'][:3]],
            'average_salary_change': '+8.5%'
        }
        
        self.log_info(f"📊 Found {total_jobs} job opportunities")
        return market_data
    
    async def _scan_job_opportunities(self, skills: List[str]) -> List[Dict[str, Any]]:
        """Scan for job opportunities"""
        opportunities = []
        
        for skill in skills[:5]:  # Limit to top 5 skills
            # Simulate job market data
            job_count = random.randint(50, 300)
            growth_rate = random.uniform(-0.1, 0.4)
            
            opportunities.append({
                'skill': skill,
                'job_count': job_count,
                'growth_rate': growth_rate,
                'demand_level': 'High' if growth_rate > 0.2 else 'Medium' if growth_rate > 0 else 'Low',
                'avg_salary': random.randint(80000, 150000),
                'remote_percentage': random.randint(60, 90)
            })
        
        return opportunities
    
    async def _analyze_salary_trends(self, skills: List[str]) -> Dict[str, Any]:
        """Analyze salary trends"""
        trends = {}
        
        for skill in skills:
            base_salary = {
                'Python': 95000, 'JavaScript': 85000, 'React': 90000,
                'Node.js': 88000, 'SQL': 75000, 'AWS': 105000
            }.get(skill, 80000)
            
            # Add some realistic variance
            current_avg = int(base_salary * random.uniform(0.95, 1.15))
            change = random.uniform(-0.05, 0.15)  # -5% to +15%
            
            trends[skill] = {
                'average_salary': current_avg,
                'change_percentage': f"{change:+.1%}",
                'trend': 'rising' if change > 0.05 else 'stable' if change > -0.02 else 'declining'
            }
        
        return trends
    
    async def _scan_company_activity(self) -> List[Dict[str, Any]]:
        """Scan company hiring activity"""
        activities = []
        
        for company in self.monitored_companies[:5]:
            # Simulate company activity
            activity_type = random.choice(['hiring_surge', 'new_funding', 'product_launch', 'expansion'])
            
            activities.append({
                'company': company,
                'activity_type': activity_type,
                'impact_score': random.uniform(0.6, 0.95),
                'hiring_likelihood': random.uniform(0.5, 0.9),
                'estimated_new_roles': random.randint(5, 50),
                'detected_at': datetime.utcnow().isoformat()
            })
        
        return activities
    
    async def _analyze_skill_trends(self, skills: List[str]) -> List[Dict[str, Any]]:
        """Analyze skill demand trends"""
        trends = []
        
        for skill in skills:
            velocity = random.uniform(-0.2, 0.3)
            demand_score = random.uniform(0.4, 0.95)
            
            trends.append({
                'name': skill,
                'demand_score': demand_score,
                'velocity': velocity,
                'trend_direction': 'rising' if velocity > 0.1 else 'stable' if velocity > -0.05 else 'declining',
                'recommendation': self._get_skill_recommendation(skill, velocity, demand_score)
            })
        
        # Sort by demand score
        trends.sort(key=lambda x: x['demand_score'], reverse=True)
        return trends
    
    def _get_skill_recommendation(self, skill: str, velocity: float, demand: float) -> str:
        """Generate skill-specific recommendations"""
        if velocity > 0.2 and demand > 0.8:
            return f"🚀 {skill} is hot! Prioritize in applications and learning."
        elif velocity > 0.1:
            return f"📈 {skill} demand is growing. Good time to strengthen this skill."
        elif velocity < -0.1:
            return f"📉 {skill} demand declining. Consider complementary skills."
        else:
            return f"📊 {skill} demand is stable. Maintain current level."
    
    def _generate_recommendations(self, data: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        # Market-based recommendations
        market_heat = data.get('market_summary', {}).get('market_heat', 'Warm')
        if market_heat == 'Hot':
            recommendations.append("🔥 Market is hot! Consider accelerating your job search timeline.")
        
        # Skill-based recommendations
        top_skills = data.get('skill_trends', [])[:2]
        for skill in top_skills:
            if skill['velocity'] > 0.2:
                recommendations.append(f"📚 Focus on {skill['name']} - showing strong growth trend.")
        
        # Company-based recommendations
        high_activity_companies = [
            comp for comp in data.get('company_activity', [])
            if comp['hiring_likelihood'] > 0.8
        ]
        
        if high_activity_companies:
            company_names = [comp['company'] for comp in high_activity_companies[:2]]
            recommendations.append(f"🎯 Monitor {', '.join(company_names)} - high hiring activity detected.")
        
        return recommendations
    
    async def generate_autonomous_tasks(self, user_id: int) -> List[Dict[str, Any]]:
        """Generate autonomous tasks for this agent"""
        tasks = []
        
        # Daily market scan
        tasks.append({
            'task_type': 'daily_market_scan',
            'description': 'Perform daily market intelligence scan',
            'user_id': user_id,
            'priority': 'high',
            'scheduled_for': datetime.utcnow() + timedelta(minutes=5),
            'context': {
                'user_skills': ['Python', 'JavaScript', 'React'],
                'target_locations': ['Remote', 'San Francisco'],
                'experience_level': 'Mid'
            }
        })
        
        return tasks

# Test the agent
async def test_market_scout():
    """Test the Market Scout Agent"""
    agent = MarketScoutAgent()
    
    # Test task execution
    test_task = {
        'task_type': 'daily_market_scan',
        'user_skills': ['Python', 'React', 'JavaScript', 'SQL'],
        'user_id': 1
    }
    
    print("🤖 Testing Market Scout Agent...")
    result = await agent.execute_task(test_task)
    
    print(f"✅ Task completed: {result.success}")
    print(f"📊 Confidence: {result.confidence_score}")
    print(f"⏱️  Execution time: {result.execution_time:.2f}s")
    
    if result.success:
        print("\n📈 Market Data:")
        print(f"  - Total opportunities: {result.data['market_summary']['total_opportunities']}")
        print(f"  - Market heat: {result.data['market_summary']['market_heat']}")
        print(f"  - Top skills: {', '.join(result.data['market_summary']['top_skills_in_demand'])}")
        
        print("\n💡 Recommendations:")
        for rec in result.recommendations:
            print(f"  - {rec}")
    
    return result

if __name__ == "__main__":
    asyncio.run(test_market_scout())
