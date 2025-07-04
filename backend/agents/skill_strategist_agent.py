
# Change line 9 from:
# from base_agent import BaseAgent, AgentResult
# 
# To:
# from .base_agent import BaseAgent, AgentResultimport asyncio
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

class SkillStrategistAgent(BaseAgent):
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("Skill Strategist", config)
        
        # AI client setup
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.log_info(f"🔑 API Key configured: {bool(self.openai_api_key and len(self.openai_api_key) > 20)}")
        
        # Skill categories and learning data
        self.skill_market_data = {
            'high_demand': ['TypeScript', 'React', 'AWS', 'Kubernetes', 'Machine Learning', 'Python'],
            'emerging': ['WebAssembly', 'Rust', 'Edge Computing', 'LangChain', 'Vector Databases'],
            'declining': ['jQuery', 'Flash', 'Perl'],
            'stable_core': ['JavaScript', 'SQL', 'Git', 'HTML/CSS']
        }
        
        self.learning_time_estimates = {
            'TypeScript': {'basic': 1, 'proficient': 3, 'advanced': 6},
            'React': {'basic': 2, 'proficient': 4, 'advanced': 8},
            'AWS': {'basic': 3, 'proficient': 6, 'advanced': 12},
            'Python': {'basic': 2, 'proficient': 4, 'advanced': 10},
            'Kubernetes': {'basic': 4, 'proficient': 8, 'advanced': 16},
            'Machine Learning': {'basic': 6, 'proficient': 12, 'advanced': 24}
        }
    
    async def execute_task(self, task_data: Dict[str, Any]) -> AgentResult:
        """Execute skill strategy tasks"""
        start_time = time.time()
        self.log_info(f"🧠 Starting task: {task_data.get('task_type', 'unknown')}")
        
        try:
            result_data = await self._analyze_skill_strategy(task_data)
            execution_time = time.time() - start_time
            
            self.stats['tasks_completed'] += 1
            self.log_info(f"✅ Task completed in {execution_time:.2f}s")
            
            return AgentResult(
                success=True,
                data=result_data,
                confidence_score=0.90,
                execution_time=execution_time,
                recommendations=self._generate_skill_recommendations(result_data)
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
    
    async def _analyze_skill_strategy(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Comprehensive skill strategy analysis using AI"""
        self.log_info("🔍 Analyzing skill strategy with AI...")
        
        current_skills = task_data.get('current_skills', ['Python', 'JavaScript'])
        target_roles = task_data.get('target_roles', ['Software Engineer'])
        experience_level = task_data.get('experience_level', 'Mid')
        
        # Analyze current skill positioning
        skill_positioning = await self._analyze_skill_positioning(current_skills)
        
        # Get AI-powered skill gap analysis
        ai_analysis = await self._ai_skill_gap_analysis(current_skills, target_roles, experience_level)
        
        # Generate learning path
        learning_path = await self._generate_optimal_learning_path(current_skills, target_roles, ai_analysis)
        
        # Calculate ROI for each skill
        skill_roi_analysis = await self._calculate_skill_roi(current_skills, target_roles)
        
        result = {
            'analysis_timestamp': datetime.now().isoformat(),
            'user_profile': {
                'current_skills': current_skills,
                'target_roles': target_roles,
                'experience_level': experience_level
            },
            'skill_positioning': skill_positioning,
            'ai_analysis': ai_analysis,
            'learning_path': learning_path,
            'skill_roi_analysis': skill_roi_analysis,
            'market_insights': await self._get_market_insights(current_skills)
        }
        
        self.log_info(f"🎯 Generated strategic skill plan with {len(learning_path.get('phases', []))} learning phases")
        return result
    
    async def _analyze_skill_positioning(self, current_skills: List[str]) -> Dict[str, Any]:
        """Analyze current skill positioning in the market"""
        
        skill_categories = {
            'high_demand': [],
            'emerging': [],
            'stable_core': [],
            'declining': [],
            'missing_high_value': []
        }
        
        current_skills_lower = [s.lower() for s in current_skills]
        
        # Categorize current skills
        for skill in current_skills:
            for category, skills_list in self.skill_market_data.items():
                if skill in skills_list:
                    skill_categories[category].append(skill)
                    break
        
        # Find missing high-value skills
        for skill in self.skill_market_data['high_demand']:
            if skill.lower() not in current_skills_lower:
                skill_categories['missing_high_value'].append(skill)
        
        # Calculate positioning score
        positioning_score = (
            len(skill_categories['high_demand']) * 10 +
            len(skill_categories['emerging']) * 8 +
            len(skill_categories['stable_core']) * 5 -
            len(skill_categories['declining']) * 3
        )
        
        return {
            'skill_categories': skill_categories,
            'positioning_score': positioning_score,
            'market_readiness': 'High' if positioning_score > 30 else 'Medium' if positioning_score > 15 else 'Developing',
            'competitive_advantage': len(skill_categories['emerging']) > 0,
            'modernization_needed': len(skill_categories['declining']) > 0
        }
    
    async def _ai_skill_gap_analysis(self, current_skills: List[str], target_roles: List[str], experience_level: str) -> Dict[str, Any]:
        """Use AI for comprehensive skill gap analysis"""
        
        if not self.openai_api_key or len(self.openai_api_key) < 20:
            return {
                'analysis': 'AI analysis unavailable - API key not configured',
                'confidence': 0.0
            }
        
        try:
            import openai
            client = openai.OpenAI(api_key=self.openai_api_key)
            
            prompt = f"""
            As an expert career strategist and technical hiring manager, analyze this skill profile for strategic career development:

            CURRENT PROFILE:
            - Skills: {', '.join(current_skills)}
            - Target Roles: {', '.join(target_roles)}
            - Experience Level: {experience_level}

            ANALYSIS REQUIRED:
            1. **Critical Skill Gaps**: What essential skills are missing for target roles?
            2. **Learning Prioritization**: Which skills should be learned first and why?
            3. **Market Positioning**: How competitive is this profile currently?
            4. **Salary Impact**: Which skills would most increase earning potential?
            5. **Future-Proofing**: What emerging skills should be considered?
            6. **Learning Strategy**: Optimal sequence and approach for skill development
            7. **Timeline**: Realistic timeline to reach target role competency

            Provide specific, actionable recommendations with reasoning. Consider current market trends and hiring demands.
            """
            
            self.log_info("🤖 Requesting AI skill analysis...")
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=1200
            )
            
            analysis_text = response.choices[0].message.content
            
            self.log_info("✅ AI skill analysis completed")
            
            return {
                'analysis': analysis_text,
                'model_used': 'gpt-3.5-turbo',
                'confidence': 0.92,
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
    
    async def _generate_optimal_learning_path(self, current_skills: List[str], target_roles: List[str], ai_analysis: Dict) -> Dict[str, Any]:
        """Generate optimized learning path"""
        
        # Determine critical skills to learn
        role_skill_requirements = {
            'Software Engineer': ['JavaScript', 'Python', 'React', 'SQL', 'Git'],
            'Senior Software Engineer': ['JavaScript', 'Python', 'React', 'TypeScript', 'AWS', 'System Design'],
            'Full Stack Developer': ['JavaScript', 'Python', 'React', 'Node.js', 'SQL', 'MongoDB'],
            'Data Scientist': ['Python', 'SQL', 'Machine Learning', 'Pandas', 'Statistics'],
            'DevOps Engineer': ['AWS', 'Docker', 'Kubernetes', 'Python', 'Linux', 'CI/CD']
        }
        
        # Get required skills for target roles
        all_required_skills = set()
        for role in target_roles:
            all_required_skills.update(role_skill_requirements.get(role, []))
        
        # Find skills to learn
        current_skills_lower = [s.lower() for s in current_skills]
        skills_to_learn = [
            skill for skill in all_required_skills 
            if skill.lower() not in current_skills_lower
        ]
        
        # Prioritize skills
        skill_priority = self._prioritize_skills(skills_to_learn, target_roles)
        
        # Generate learning phases
        phases = []
        current_week = 0
        
        for i, skill_info in enumerate(skill_priority[:5]):  # Top 5 skills
            skill = skill_info['skill']
            weeks_needed = skill_info['learning_time_weeks']
            
            phase = {
                'phase_number': i + 1,
                'skill': skill,
                'start_week': current_week + 1,
                'end_week': current_week + weeks_needed,
                'duration_weeks': weeks_needed,
                'learning_approach': self._get_learning_approach(skill),
                'practice_projects': self._get_practice_projects(skill),
                'milestone_goals': self._get_milestone_goals(skill),
                'resources': self._get_learning_resources(skill),
                'priority_reason': skill_info['priority_reason']
            }
            
            phases.append(phase)
            current_week += weeks_needed
        
        return {
            'total_duration_weeks': current_week,
            'phases': phases,
            'skills_to_learn': skills_to_learn,
            'learning_strategy': 'Sequential with parallel practice projects',
            'success_metrics': self._define_success_metrics(skills_to_learn)
        }
    
    def _prioritize_skills(self, skills_to_learn: List[str], target_roles: List[str]) -> List[Dict[str, Any]]:
        """Prioritize skills by impact and market demand"""
        
        skill_priorities = []
        
        # Priority weights
        demand_weights = {
            'TypeScript': 9, 'React': 9, 'AWS': 10, 'Python': 8,
            'Node.js': 7, 'Docker': 8, 'Kubernetes': 9,
            'Machine Learning': 10, 'SQL': 6, 'Git': 5
        }
        
        for skill in skills_to_learn:
            demand_weight = demand_weights.get(skill, 5)
            learning_time = self.learning_time_estimates.get(skill, {'proficient': 4})['proficient']
            
            # Calculate priority score (higher demand, lower learning time = higher priority)
            priority_score = demand_weight * 10 - learning_time
            
            skill_priorities.append({
                'skill': skill,
                'priority_score': priority_score,
                'learning_time_weeks': learning_time,
                'market_demand': demand_weight,
                'salary_impact': f"+${demand_weight * 1000 + random.randint(1000, 3000)}",
                'priority_reason': self._get_priority_reason(skill, demand_weight, learning_time)
            })
        
        # Sort by priority score
        skill_priorities.sort(key=lambda x: x['priority_score'], reverse=True)
        return skill_priorities
    
    def _get_priority_reason(self, skill: str, demand: int, time: int) -> str:
        """Get reasoning for skill priority"""
        if demand >= 9:
            return f"Critical high-demand skill with strong ROI"
        elif time <= 2:
            return f"Quick win - can be learned rapidly"
        elif demand >= 7:
            return f"Solid market demand with good career impact"
        else:
            return f"Important foundational skill for target roles"
    
    def _get_learning_approach(self, skill: str) -> str:
        """Get recommended learning approach"""
        approaches = {
            'TypeScript': 'Gradual adoption in existing projects',
            'React': 'Project-based learning with hooks and modern patterns',
            'AWS': 'Hands-on labs with certification track',
            'Python': 'Practical automation and data projects',
            'Kubernetes': 'Container orchestration labs',
            'Machine Learning': 'Kaggle competitions and real datasets'
        }
        return approaches.get(skill, f'Structured course with hands-on projects')
    
    def _get_practice_projects(self, skill: str) -> List[str]:
        """Get practice project suggestions"""
        projects = {
            'TypeScript': ['Convert existing JS project', 'Build type-safe API client'],
            'React': ['Personal portfolio site', 'Todo app with hooks', 'Weather dashboard'],
            'AWS': ['Deploy static website', 'Serverless API', 'Auto-scaling web app'],
            'Python': ['Web scraper', 'Data analysis tool', 'REST API'],
            'Kubernetes': ['Deploy microservices', 'Set up CI/CD pipeline'],
            'Machine Learning': ['Prediction model', 'Classification project', 'Recommendation system']
        }
        return projects.get(skill, [f'{skill} portfolio project', f'Industry-relevant {skill} demo'])
    
    def _get_milestone_goals(self, skill: str) -> List[str]:
        """Get milestone goals for skill development"""
        return [
            f'Complete {skill} fundamentals course',
            f'Build first {skill} project',
            f'Contribute to open source {skill} project',
            f'Add {skill} to professional portfolio'
        ]
    
    def _get_learning_resources(self, skill: str) -> List[str]:
        """Get curated learning resources"""
        resources = {
            'TypeScript': ['TypeScript Handbook', 'React + TypeScript Course', 'TypeScript Deep Dive'],
            'React': ['React Official Docs', 'Full Stack Open', 'React Query Tutorial'],
            'AWS': ['AWS Training', 'A Cloud Guru', 'AWS Solutions Architect Course'],
            'Python': ['Automate the Boring Stuff', 'Real Python', 'Python Crash Course'],
            'Kubernetes': ['Kubernetes Official Docs', 'Kubernetes Up & Running', 'CKA Certification']
        }
        return resources.get(skill, [f'{skill} Official Documentation', f'{skill} Crash Course'])
    
    def _define_success_metrics(self, skills: List[str]) -> List[str]:
        """Define success metrics for learning plan"""
        return [
            'Build portfolio project using each new skill',
            'Pass technical interviews focusing on learned skills',
            'Contribute to open source projects',
            'Achieve relevant certifications where applicable',
            'Successfully transition to target role within timeline'
        ]
    
    async def _calculate_skill_roi(self, current_skills: List[str], target_roles: List[str]) -> Dict[str, Any]:
        """Calculate ROI for different skills"""
        
        high_roi_skills = {
            'AWS': {'salary_increase': 12000, 'job_opportunities': '+40%', 'learning_time': 6},
            'TypeScript': {'salary_increase': 8000, 'job_opportunities': '+25%', 'learning_time': 3},
            'React': {'salary_increase': 10000, 'job_opportunities': '+35%', 'learning_time': 4},
            'Kubernetes': {'salary_increase': 15000, 'job_opportunities': '+50%', 'learning_time': 8},
            'Machine Learning': {'salary_increase': 20000, 'job_opportunities': '+60%', 'learning_time': 12}
        }
        
        roi_analysis = {}
        for skill, data in high_roi_skills.items():
            if skill.lower() not in [s.lower() for s in current_skills]:
                roi_score = data['salary_increase'] / data['learning_time']  # ROI per week
                roi_analysis[skill] = {
                    **data,
                    'roi_score': roi_score,
                    'payback_period_months': round(data['learning_time'] / 4.33, 1),  # weeks to months
                    'recommendation': 'High Priority' if roi_score > 1500 else 'Medium Priority'
                }
        
        return roi_analysis
    
    async def _get_market_insights(self, current_skills: List[str]) -> Dict[str, Any]:
        """Get current market insights"""
        return {
            'trending_skills': ['AI/ML', 'TypeScript', 'Kubernetes', 'Rust', 'WebAssembly'],
            'skill_salary_trends': {
                'AI/ML': '+15% this year',
                'TypeScript': '+12% this year',
                'Kubernetes': '+18% this year'
            },
            'market_advice': 'Focus on cloud-native and AI-adjacent skills for maximum ROI',
            'industry_shifts': [
                'Increased demand for TypeScript over vanilla JavaScript',
                'Container orchestration becoming standard',
                'AI integration skills highly valued'
            ]
        }
    
    def _generate_skill_recommendations(self, data: Dict[str, Any]) -> List[str]:
        """Generate actionable skill recommendations"""
        recommendations = []
        
        # AI insights
        ai_analysis = data.get('ai_analysis', {})
        if ai_analysis.get('confidence', 0) > 0.5:
            recommendations.append("🤖 Comprehensive AI skill analysis available below")
        
        # Learning path insights
        learning_path = data.get('learning_path', {})
        if learning_path.get('phases'):
            first_skill = learning_path['phases'][0]['skill']
            duration = learning_path['phases'][0]['duration_weeks']
            recommendations.append(f"🎯 Start with {first_skill} - {duration} week focused learning plan")
        
        # ROI insights
        roi_analysis = data.get('skill_roi_analysis', {})
        high_roi_skills = [skill for skill, data in roi_analysis.items() if data.get('roi_score', 0) > 1500]
        if high_roi_skills:
            recommendations.append(f"💰 High ROI skills: {', '.join(high_roi_skills[:2])}")
        
        # Positioning insights
        positioning = data.get('skill_positioning', {})
        if positioning.get('modernization_needed'):
            recommendations.append("🔄 Update legacy skills to modern alternatives")
        
        recommendations.extend([
            "📚 Combine theoretical learning with practical projects",
            "🏆 Target relevant certifications for credibility",
            "📈 Track progress with portfolio development"
        ])
        
        return recommendations
    
    async def generate_autonomous_tasks(self, user_id: int) -> List[Dict[str, Any]]:
        """Generate autonomous skill strategy tasks"""
        return [{
            'task_type': 'skill_gap_analysis',
            'description': 'AI-powered skill strategy analysis',
            'user_id': user_id,
            'priority': 'high',
            'context': {
                'current_skills': ['Python', 'JavaScript', 'React'],
                'target_roles': ['Senior Software Engineer'],
                'experience_level': 'Mid'
            }
        }]

# Test function
async def test_skill_strategist():
    """Test the AI-powered Skill Strategist Agent"""
    agent = SkillStrategistAgent()
    
    test_task = {
        'task_type': 'skill_gap_analysis',
        'current_skills': ['Python', 'JavaScript', 'HTML', 'CSS', 'SQL'],
        'target_roles': ['Senior Software Engineer', 'Full Stack Developer'],
        'experience_level': 'Mid',
        'user_id': 1
    }
    
    print("🧠 Testing AI-Powered Skill Strategist Agent...")
    print("=" * 65)
    
    result = await agent.execute_task(test_task)
    
    print(f"✅ Success: {result.success}")
    print(f"📊 Confidence: {result.confidence_score:.1%}")
    print(f"⏱️  Time: {result.execution_time:.2f}s")
    print("=" * 65)
    
    if result.success:
        data = result.data
        
        # Show skill positioning
        positioning = data.get('skill_positioning', {})
        print(f"\n📊 CURRENT SKILL POSITIONING:")
        print(f"  Market Readiness: {positioning.get('market_readiness', 'Unknown')}")
        print(f"  Positioning Score: {positioning.get('positioning_score', 0)}")
        print(f"  High-Demand Skills: {len(positioning.get('skill_categories', {}).get('high_demand', []))}")
        print(f"  Missing High-Value: {len(positioning.get('skill_categories', {}).get('missing_high_value', []))}")
        
        # Show learning path
        learning_path = data.get('learning_path', {})
        if learning_path.get('phases'):
            print(f"\n📅 LEARNING PATH ({learning_path.get('total_duration_weeks', 0)} weeks total):")
            print("-" * 50)
            
            for phase in learning_path['phases'][:3]:  # Show first 3 phases
                print(f"Phase {phase['phase_number']}: {phase['skill']}")
                print(f"  📅 Weeks {phase['start_week']}-{phase['end_week']} ({phase['duration_weeks']} weeks)")
                print(f"  🎯 Approach: {phase['learning_approach']}")
                print(f"  💡 Why: {phase['priority_reason']}")
                print(f"  📂 Projects: {', '.join(phase['practice_projects'][:2])}")
        
        # Show ROI analysis
        roi_analysis = data.get('skill_roi_analysis', {})
        if roi_analysis:
            print(f"\n💰 SKILL ROI ANALYSIS:")
            print("-" * 30)
            for skill, roi_data in list(roi_analysis.items())[:3]:
                print(f"{skill}: +${roi_data['salary_increase']:,} | {roi_data['job_opportunities']} jobs | {roi_data['learning_time']} weeks")
        
        # Show AI analysis
        ai_analysis = data.get('ai_analysis', {})
        if ai_analysis.get('confidence', 0) > 0.5:
            print(f"\n🤖 AI STRATEGIC ANALYSIS:")
            print(f"   Model: {ai_analysis.get('model_used')}")
            print(f"   Confidence: {ai_analysis.get('confidence', 0):.1%}")
            print("-" * 50)
            analysis_text = ai_analysis.get('analysis', '')
            # Show first 400 characters
            print(analysis_text[:400] + "..." if len(analysis_text) > 400 else analysis_text)
        
        # Show recommendations
        print(f"\n💡 STRATEGIC RECOMMENDATIONS:")
        for i, rec in enumerate(result.recommendations, 1):
            print(f"   {i}. {rec}")
    
    print("\n" + "=" * 65)
    return result

if __name__ == "__main__":
    asyncio.run(test_skill_strategist())
