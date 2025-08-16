#!/usr/bin/env python3
"""
Enhanced Hybrid Career Intelligence Orchestrator

Combines:
1. Jobright.ai integration (job discovery + auto-apply)  
2. Best-in-class resume optimization (Jobscan + Teal)
3. Your advanced AI agents (CrewAI, LangChain, Vector DB)
4. NEW: Precision Career Transition Intelligence Layer

This creates the most sophisticated career intelligence system available.
"""

import asyncio
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class PrecisionJobApplication:
    """A precision-targeted job application with complete intelligence"""
    job_match: Any  # JobMatch from Jobright.ai
    transition_analysis: Any  # CareerTransitionPath from precision layer
    optimized_materials: Dict[str, Any]  # From Jobscan + Teal
    ai_strategy: Dict[str, Any]  # From your AI agents
    precision_targeting: Dict[str, Any]  # From precision layer
    application_timeline: Dict[str, Any]
    success_prediction: float
    strategic_value: float

class EnhancedHybridOrchestrator:
    """
    Master orchestrator combining all intelligence layers for unprecedented precision
    """
    
    def __init__(self):
        # External service integrations
        from ai.jobright_integration import JobrightIntegration
        self.jobright = JobrightIntegration()
        
        # Your advanced AI system
        from ai.crewai_career_agents import CrewAICareerSystem
        from ai.vector_career_db import VectorCareerDatabase
        from ai.langchain_career_agent import LangChainCareerAgent
        from ai.precision_career_transition_intelligence import PrecisionCareerTransitionIntelligence
        
        self.crew_ai = CrewAICareerSystem()
        self.vector_db = VectorCareerDatabase()
        self.langchain_agent = LangChainCareerAgent()
        self.precision_intel = PrecisionCareerTransitionIntelligence()
        
        # Mock external APIs (replace with real integrations)
        self.jobscan_api = self._mock_jobscan_api()
        self.teal_api = self._mock_teal_api()
    
    async def execute_precision_career_intelligence_workflow(self, 
                                                           user_profile: Dict[str, Any],
                                                           career_goals: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the complete precision career intelligence workflow
        """
        
        print("🚀 Starting Enhanced Hybrid Career Intelligence Workflow...")
        print("=" * 70)
        
        # Phase 1: Precision Career Transition Analysis
        print("\n🎯 Phase 1: Precision Career Transition Analysis")
        transition_paths = await self.precision_intel.analyze_precision_career_transitions(
            user_profile, career_goals
        )
        
        # Phase 2: Strategic Job Discovery 
        print("\n🔍 Phase 2: Strategic Job Discovery (Jobright.ai)")
        job_matches = await self.jobright.find_job_matches(user_profile, career_goals)
        
        # Phase 3: Intelligent Job-Transition Alignment
        print("\n🧠 Phase 3: Intelligent Job-Transition Alignment")
        aligned_opportunities = await self._align_jobs_with_transitions(
            job_matches, transition_paths, user_profile
        )
        
        # Phase 4: Precision Application Creation
        print("\n📋 Phase 4: Precision Application Creation")
        precision_applications = await self._create_precision_applications(
            aligned_opportunities, user_profile
        )
        
        # Phase 5: Strategic Execution Planning
        print("\n🎯 Phase 5: Strategic Execution Planning")
        execution_plan = await self._create_strategic_execution_plan(
            precision_applications, user_profile
        )
        
        return {
            'transition_intelligence': {
                'paths_analyzed': len(transition_paths),
                'strategic_transitions': [p for p in transition_paths if p.success_probability > 0.7],
                'top_transition': transition_paths[0] if transition_paths else None
            },
            'job_discovery': {
                'jobs_found': len(job_matches),
                'precision_aligned': len(aligned_opportunities),
                'high_value_targets': len([app for app in precision_applications if app.strategic_value > 0.8])
            },
            'precision_applications': precision_applications,
            'execution_plan': execution_plan,
            'competitive_advantages': self._identify_competitive_advantages(precision_applications),
            'success_metrics': self._calculate_success_metrics(precision_applications)
        }
    
    async def _align_jobs_with_transitions(self, 
                                         job_matches: List[Any],
                                         transition_paths: List[Any],
                                         user_profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Intelligently align job opportunities with strategic career transitions
        """
        
        aligned_opportunities = []
        
        for job in job_matches:
            best_transition_alignment = None
            best_alignment_score = 0.0
            
            # Find the best transition path alignment for this job
            for transition in transition_paths:
                alignment_score = await self._calculate_job_transition_alignment(
                    job, transition, user_profile
                )
                
                if alignment_score > best_alignment_score:
                    best_alignment_score = alignment_score
                    best_transition_alignment = transition
            
            # Only include jobs with strong transition alignment
            if best_alignment_score > 0.6:
                
                # Use your AI agents to analyze strategic fit
                crew_analysis = await self.crew_ai.analyze_strategic_job_fit({
                    'job': job,
                    'transition_path': best_transition_alignment,
                    'user_profile': user_profile,
                    'alignment_score': best_alignment_score
                })
                
                # Check against historical patterns
                similar_transitions = self.vector_db.semantic_job_search(
                    f"{job.title} at {job.company} from {user_profile.get('current_role', '')}",
                    n_results=3
                )
                
                aligned_opportunities.append({
                    'job': job,
                    'transition_path': best_transition_alignment,
                    'alignment_score': best_alignment_score,
                    'crew_analysis': crew_analysis,
                    'historical_patterns': similar_transitions,
                    'strategic_value': best_alignment_score * job.match_percentage * best_transition_alignment.success_probability
                })
        
        # Sort by strategic value
        return sorted(aligned_opportunities, key=lambda x: x['strategic_value'], reverse=True)
    
    async def _create_precision_applications(self, 
                                           aligned_opportunities: List[Dict[str, Any]],
                                           user_profile: Dict[str, Any]) -> List[PrecisionJobApplication]:
        """
        Create precision-targeted applications combining all intelligence layers
        """
        
        precision_applications = []
        
        for opportunity in aligned_opportunities:
            job = opportunity['job']
            transition_path = opportunity['transition_path']
            
            print(f"   Creating precision application for {job.title} at {job.company}...")
            
            # 1. Generate optimized materials (Jobscan + Teal, NOT Jobright's weak resume tools)
            base_resume = await self.teal_api.generate_resume(job, user_profile)
            ats_optimized_resume = await self.jobscan_api.optimize_for_ats(base_resume, job)
            cover_letter = await self.teal_api.generate_cover_letter(job, user_profile, transition_path)
            
            optimized_materials = {
                'resume': ats_optimized_resume,
                'cover_letter': cover_letter,
                'ats_score': ats_optimized_resume.get('ats_score', 0.8),
                'optimization_summary': ats_optimized_resume.get('improvements', [])
            }
            
            # 2. Create AI-powered application strategy
            ai_strategy = await self.crew_ai.create_precision_application_strategy({
                'job': job,
                'transition_path': transition_path,
                'user_profile': user_profile,
                'historical_success': opportunity['historical_patterns'],
                'materials': optimized_materials
            })
            
            # 3. Apply precision targeting from transition intelligence
            precision_targeting = {
                'networking_strategy': transition_path.precision_strategy.get('networking_targets', []),
                'skill_positioning': self._create_skill_positioning_strategy(transition_path, job),
                'company_insider_insights': await self.jobright.get_insider_connections(job, user_profile),
                'application_timing': transition_path.precision_strategy.get('application_timing', {}),
                'success_accelerators': transition_path.precision_strategy.get('success_accelerators', [])
            }
            
            # 4. Calculate timeline and success prediction
            application_timeline = self._create_application_timeline(transition_path, precision_targeting)
            
            success_prediction = self._calculate_application_success_prediction(
                job, transition_path, optimized_materials, ai_strategy, precision_targeting
            )
            
            precision_app = PrecisionJobApplication(
                job_match=job,
                transition_analysis=transition_path,
                optimized_materials=optimized_materials,
                ai_strategy=ai_strategy,
                precision_targeting=precision_targeting,
                application_timeline=application_timeline,
                success_prediction=success_prediction,
                strategic_value=opportunity['strategic_value']
            )
            
            precision_applications.append(precision_app)
        
        return precision_applications
    
    async def _create_strategic_execution_plan(self, 
                                             precision_applications: List[PrecisionJobApplication],
                                             user_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create strategic execution plan for precision applications
        """
        
        # Prioritize applications by strategic value and success prediction
        top_applications = sorted(precision_applications, 
                                key=lambda x: x.success_prediction * x.strategic_value, 
                                reverse=True)
        
        execution_phases = {
            'immediate_action': {
                'timeline': 'Next 2 weeks',
                'applications': top_applications[:3],
                'focus': 'Highest probability + highest strategic value',
                'actions': [
                    'Apply to top 3 strategic opportunities',
                    'Initiate networking outreach',
                    'Begin skill development for top transition path'
                ]
            },
            'strategic_preparation': {
                'timeline': 'Weeks 3-6',
                'applications': top_applications[3:8],
                'focus': 'Medium-term strategic opportunities',
                'actions': [
                    'Complete priority skill certifications',
                    'Build demonstration projects',
                    'Expand professional network'
                ]
            },
            'portfolio_expansion': {
                'timeline': 'Weeks 7-12',
                'applications': top_applications[8:],
                'focus': 'Broader opportunity exploration',
                'actions': [
                    'Apply to exploratory opportunities',
                    'Test additional transition paths',
                    'Build comprehensive portfolio'
                ]
            }
        }
        
        return {
            'execution_phases': execution_phases,
            'weekly_schedule': self._create_weekly_execution_schedule(top_applications),
            'success_tracking_kpis': self._define_success_kpis(),
            'risk_mitigation': self._identify_risks_and_mitigations(top_applications),
            'competitive_differentiation': self._create_differentiation_strategy(user_profile, top_applications)
        }
    
    async def _calculate_job_transition_alignment(self, 
                                                job: Any, 
                                                transition: Any, 
                                                user_profile: Dict[str, Any]) -> float:
        """Calculate alignment between job and transition path"""
        
        # Factors that contribute to alignment
        company_alignment = 1.0 if job.company == transition.target_company else 0.7
        role_alignment = self._calculate_role_similarity(job.title, transition.to_role)
        skill_alignment = self._calculate_skill_overlap(job.requirements, transition.required_skills)
        
        # Weight the factors
        alignment_score = (
            company_alignment * 0.3 +
            role_alignment * 0.4 +
            skill_alignment * 0.3
        )
        
        return min(1.0, alignment_score)
    
    def _create_skill_positioning_strategy(self, transition_path: Any, job: Any) -> Dict[str, Any]:
        """Create strategy for positioning skills for this specific transition"""
        return {
            'highlight_transferable': [skill.skill_name for skill in transition_path.required_skills[:3]],
            'address_gaps': transition_path.skill_gaps[:2],
            'unique_differentiators': ['Cross-functional experience', 'Technical depth'],
            'positioning_narrative': f'Leveraging {transition_path.from_role} experience to excel in {transition_path.to_role}'
        }
    
    def _create_application_timeline(self, transition_path: Any, precision_targeting: Dict[str, Any]) -> Dict[str, Any]:
        """Create detailed application timeline"""
        return {
            'preparation_phase': '1-2 weeks',
            'networking_outreach': 'Week 1-3',
            'application_submission': 'Week 2',
            'follow_up_schedule': ['1 week', '2 weeks', '1 month'],
            'skill_development_parallel': f'{transition_path.timeline_months} months'
        }
    
    def _calculate_application_success_prediction(self, job, transition_path, materials, ai_strategy, precision_targeting) -> float:
        """Calculate overall success prediction for this application"""
        
        factors = {
            'job_match_score': job.match_percentage,
            'transition_success_probability': transition_path.success_probability,
            'ats_optimization_score': materials['ats_score'],
            'ai_strategy_confidence': ai_strategy.get('confidence', 0.8),
            'networking_advantage': len(precision_targeting.get('company_insider_insights', {}).get('direct_connections', [])) * 0.1,
            'timing_advantage': 0.1 if precision_targeting.get('application_timing', {}).get('current_market_condition') == 'favorable' else 0.0
        }
        
        # Weighted success prediction
        success_prediction = (
            factors['job_match_score'] * 0.25 +
            factors['transition_success_probability'] * 0.25 +
            factors['ats_optimization_score'] * 0.2 +
            factors['ai_strategy_confidence'] * 0.15 +
            factors['networking_advantage'] * 0.1 +
            factors['timing_advantage'] * 0.05
        )
        
        return min(0.95, success_prediction)
    
    def _identify_competitive_advantages(self, precision_applications: List[PrecisionJobApplication]) -> List[str]:
        """Identify key competitive advantages of this approach"""
        return [
            "Precision job-transition alignment vs random applications",
            "Best-in-class ATS optimization (avoiding weak Jobright resume tools)",
            "Historical pattern analysis from 266+ application dataset", 
            "Multi-agent AI strategy vs single-point solutions",
            "Company insider intelligence and networking strategies",
            "Strategic timing and market condition analysis"
        ]
    
    def _calculate_success_metrics(self, precision_applications: List[PrecisionJobApplication]) -> Dict[str, Any]:
        """Calculate expected success metrics"""
        
        if not precision_applications:
            return {}
        
        avg_success_prediction = sum(app.success_prediction for app in precision_applications) / len(precision_applications)
        high_confidence_apps = [app for app in precision_applications if app.success_prediction > 0.8]
        
        return {
            'average_success_prediction': f"{avg_success_prediction:.1%}",
            'high_confidence_applications': len(high_confidence_apps),
            'expected_interview_rate': f"{avg_success_prediction * 1.2:.1%}",  # Higher than success prediction
            'strategic_transition_probability': f"{max(app.transition_analysis.success_probability for app in precision_applications):.1%}",
            'time_to_success_estimate': '3-6 months'
        }
    
    # Mock API implementations (replace with real integrations)
    def _mock_jobscan_api(self):
        """Mock Jobscan API"""
        class MockJobscanAPI:
            async def optimize_for_ats(self, resume, job):
                return {
                    'optimized_resume': resume + " [ATS OPTIMIZED]",
                    'ats_score': 0.87,
                    'improvements': ['Added relevant keywords', 'Improved formatting', 'Enhanced skills section']
                }
        return MockJobscanAPI()
    
    def _mock_teal_api(self):
        """Mock Teal API"""
        class MockTealAPI:
            async def generate_resume(self, job, profile):
                return f"AI-Generated Resume for {job.title} at {job.company}"
            
            async def generate_cover_letter(self, job, profile, transition):
                return f"AI-Generated Cover Letter for transition to {job.title}"
        return MockTealAPI()
    
    # Additional helper methods (simplified)
    def _calculate_role_similarity(self, job_title: str, target_role: str) -> float:
        """Calculate similarity between job title and target role"""
        return 0.8  # Mock calculation
    
    def _calculate_skill_overlap(self, job_requirements: List[str], required_skills: List[Any]) -> float:
        """Calculate overlap between job requirements and required skills"""
        return 0.75  # Mock calculation
    
    def _create_weekly_execution_schedule(self, applications: List[PrecisionJobApplication]) -> Dict[str, List[str]]:
        """Create weekly execution schedule"""
        return {
            'Week 1': ['Apply to top 2 opportunities', 'Begin networking outreach'],
            'Week 2': ['Apply to next 3 opportunities', 'Follow up on Week 1 applications'],
            'Week 3': ['Skill development focus', 'Continued networking'],
            'Week 4': ['Portfolio updates', 'Interview preparation']
        }
    
    def _define_success_kpis(self) -> List[str]:
        """Define success KPIs"""
        return [
            'Application-to-interview rate > 25%',
            'Interview-to-offer rate > 40%', 
            'Strategic transition completion < 12 months',
            'Salary increase > 20%'
        ]
    
    def _identify_risks_and_mitigations(self, applications: List[PrecisionJobApplication]) -> Dict[str, str]:
        """Identify risks and mitigation strategies"""
        return {
            'Market downturn': 'Focus on recession-proof roles and companies',
            'Skill gap concerns': 'Accelerated certification and project development',
            'Network limitations': 'Strategic networking expansion and referral programs',
            'Timeline pressure': 'Parallel preparation and multiple pathway approach'
        }
    
    def _create_differentiation_strategy(self, profile: Dict[str, Any], applications: List[PrecisionJobApplication]) -> Dict[str, Any]:
        """Create competitive differentiation strategy"""
        return {
            'unique_value_proposition': 'Cross-functional expertise with proven transition capability',
            'narrative_positioning': 'Strategic career evolution vs random job seeking',
            'evidence_portfolio': 'Demonstrate transition readiness through targeted projects',
            'network_leverage': 'Utilize insider connections and referral strategies'
        }

# Example usage
async def demo_enhanced_hybrid_orchestrator():
    """Demonstrate the enhanced hybrid orchestrator"""
    
    orchestrator = EnhancedHybridOrchestrator()
    
    user_profile = {
        'current_role': 'Senior Software Engineer',
        'skills': ['Python', 'Machine Learning', 'System Design', 'Leadership'],
        'experience_years': 7,
        'industry': 'Technology',
        'company': 'Current Tech Company'
    }
    
    career_goals = {
        'target_companies': ['Google', 'Amazon', 'Microsoft'],
        'target_roles': ['Product Manager', 'Engineering Manager'],
        'timeline_months': 12,
        'salary_increase_target': 0.25,
        'transition_priority': 'strategic_growth'
    }
    
    results = await orchestrator.execute_precision_career_intelligence_workflow(
        user_profile, career_goals
    )
    
    print("\n🎯 ENHANCED HYBRID ORCHESTRATOR RESULTS")
    print("=" * 50)
    
    print(f"\n🔍 Transition Intelligence:")
    print(f"  • Strategic Paths: {len(results['transition_intelligence']['strategic_transitions'])}")
    print(f"  • Top Transition Success Rate: {results['transition_intelligence']['top_transition'].success_probability:.1%}")
    
    print(f"\n📋 Job Discovery & Alignment:")
    print(f"  • Jobs Found: {results['job_discovery']['jobs_found']}")
    print(f"  • Precision Aligned: {results['job_discovery']['precision_aligned']}")
    print(f"  • High-Value Targets: {results['job_discovery']['high_value_targets']}")
    
    print(f"\n🚀 Success Metrics:")
    for metric, value in results['success_metrics'].items():
        print(f"  • {metric.replace('_', ' ').title()}: {value}")
    
    print(f"\n🎯 Competitive Advantages:")
    for advantage in results['competitive_advantages'][:3]:
        print(f"  • {advantage}")

if __name__ == "__main__":
    asyncio.run(demo_enhanced_hybrid_orchestrator())