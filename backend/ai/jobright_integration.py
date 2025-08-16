#!/usr/bin/env python3
"""
Jobright.ai Integration Module
Focuses on their strongest features: Job Matching + Auto-Application
Avoids their weak resume optimization in favor of better alternatives
"""

import asyncio
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class JobMatch:
    """Job match from Jobright.ai with scoring"""
    job_id: str
    title: str
    company: str
    location: str
    description: str
    requirements: List[str]
    salary_range: Optional[str]
    match_percentage: float
    jobright_score: float
    application_deadline: Optional[datetime]
    source_url: str

class JobrightIntegration:
    """
    Integration with Jobright.ai focusing on their core strengths:
    1. Job matching and scoring
    2. Auto-application capabilities
    3. Daily job discovery (400K+ jobs)
    
    AVOIDING: Their resume optimization (use Jobscan/Enhancv instead)
    """
    
    def __init__(self):
        self.api_key = os.getenv('JOBRIGHT_API_KEY')
        self.base_url = "https://api.jobright.ai/v1"
        self.daily_job_limit = 50  # Configurable limit
        
    async def find_job_matches(self, user_profile: Dict[str, Any], preferences: Dict[str, Any]) -> List[JobMatch]:
        """
        Use Jobright.ai's job matching engine (their strength)
        Returns scored job matches without using their resume features
        """
        try:
            # Mock implementation - replace with actual Jobright.ai API calls
            payload = {
                'profile': {
                    'skills': user_profile.get('skills', []),
                    'experience_years': user_profile.get('experience_years', 0),
                    'education': user_profile.get('education', ''),
                    'current_role': user_profile.get('current_role', ''),
                    'industry_preference': user_profile.get('industry', '')
                },
                'preferences': {
                    'locations': preferences.get('locations', []),
                    'remote_ok': preferences.get('remote_ok', True),
                    'salary_min': preferences.get('salary_min', 0),
                    'job_types': preferences.get('job_types', ['full-time']),
                    'company_sizes': preferences.get('company_sizes', ['any'])
                },
                'filters': {
                    'daily_limit': self.daily_job_limit,
                    'match_threshold': preferences.get('match_threshold', 0.6),
                    'include_auto_apply': True
                }
            }
            
            # Simulated API response structure
            mock_matches = [
                JobMatch(
                    job_id="jr_001",
                    title="Senior Data Engineer",
                    company="TechCorp Inc",
                    location="San Francisco, CA",
                    description="Build scalable data pipelines using Python, Spark, and AWS...",
                    requirements=["Python", "Apache Spark", "AWS", "5+ years experience"],
                    salary_range="$150,000 - $200,000",
                    match_percentage=0.89,
                    jobright_score=0.92,
                    application_deadline=None,
                    source_url="https://techcorp.com/careers/senior-data-engineer"
                ),
                JobMatch(
                    job_id="jr_002", 
                    title="ML Engineering Manager",
                    company="AI Startup",
                    location="Remote",
                    description="Lead ML engineering team to build production ML systems...",
                    requirements=["Machine Learning", "Python", "Team Leadership", "MLOps"],
                    salary_range="$180,000 - $220,000",
                    match_percentage=0.84,
                    jobright_score=0.88,
                    application_deadline=None,
                    source_url="https://aistartup.com/jobs/ml-eng-manager"
                )
            ]
            
            print(f"✅ Found {len(mock_matches)} job matches from Jobright.ai")
            return mock_matches
            
        except Exception as e:
            print(f"❌ Jobright.ai job matching failed: {e}")
            return []
    
    async def get_insider_connections(self, job_match: JobMatch, user_linkedin_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Use Jobright.ai's networking feature to find connections at target companies
        This is one of their unique value-adds
        """
        try:
            # Mock implementation
            connections = {
                'direct_connections': [
                    {
                        'name': 'Sarah Johnson',
                        'title': 'Senior Data Scientist',
                        'company': job_match.company,
                        'connection_degree': 1,
                        'mutual_connections': 3,
                        'linkedin_url': 'https://linkedin.com/in/sarahjohnson',
                        'referral_likelihood': 0.7
                    }
                ],
                'second_degree': [
                    {
                        'name': 'Mike Chen',
                        'title': 'Engineering Director', 
                        'company': job_match.company,
                        'connection_degree': 2,
                        'mutual_connections': 1,
                        'linkedin_url': 'https://linkedin.com/in/mikechen',
                        'referral_likelihood': 0.4
                    }
                ],
                'company_insights': {
                    'total_employees': 1250,
                    'hiring_velocity': 'high',
                    'recent_funding': '$50M Series B',
                    'growth_stage': 'scale-up'
                }
            }
            
            print(f"✅ Found {len(connections['direct_connections'])} direct connections at {job_match.company}")
            return connections
            
        except Exception as e:
            print(f"❌ Insider connections lookup failed: {e}")
            return {'direct_connections': [], 'second_degree': []}
    
    async def auto_apply_with_intelligence(self, job_match: JobMatch, optimized_materials: Dict[str, Any], ai_strategy: Dict[str, Any]) -> Dict[str, Any]:
        """
        Use Jobright.ai's auto-application system (their strength)
        Combined with materials optimized by better services (Jobscan/Teal, not Jobright's resume tools)
        """
        try:
            application_data = {
                'job_id': job_match.job_id,
                'materials': {
                    'resume': optimized_materials['resume'],  # From Teal/Jobscan, not Jobright
                    'cover_letter': optimized_materials['cover_letter'],
                    'portfolio_links': optimized_materials.get('portfolio_links', [])
                },
                'personalization': {
                    'why_interested': ai_strategy.get('company_interest', ''),
                    'key_qualifications': ai_strategy.get('top_qualifications', []),
                    'customized_pitch': ai_strategy.get('elevator_pitch', '')
                },
                'application_settings': {
                    'follow_up_enabled': True,
                    'track_application': True,
                    'notify_on_response': True
                }
            }
            
            # Mock successful application
            application_result = {
                'application_id': f"app_{job_match.job_id}_{datetime.now().strftime('%Y%m%d_%H%M')}",
                'status': 'submitted',
                'submitted_at': datetime.now(),
                'tracking_url': f"https://jobright.ai/applications/app_{job_match.job_id}",
                'estimated_response_time': '3-5 business days',
                'next_steps': [
                    'Application submitted successfully',
                    'Follow-up reminder set for 1 week',
                    'Connection outreach scheduled'
                ]
            }
            
            print(f"✅ Auto-applied to {job_match.title} at {job_match.company}")
            return application_result
            
        except Exception as e:
            print(f"❌ Auto-application failed: {e}")
            return {'status': 'failed', 'error': str(e)}
    
    async def track_application_status(self, application_id: str) -> Dict[str, Any]:
        """Track application status using Jobright.ai's tracking system"""
        try:
            # Mock tracking response
            status = {
                'application_id': application_id,
                'current_status': 'under_review',
                'status_history': [
                    {'status': 'submitted', 'timestamp': '2025-01-15T10:00:00Z'},
                    {'status': 'viewed', 'timestamp': '2025-01-16T14:30:00Z'},
                    {'status': 'under_review', 'timestamp': '2025-01-17T09:15:00Z'}
                ],
                'estimated_next_update': '2025-01-20',
                'recruiter_activity': {
                    'profile_views': 2,
                    'last_activity': '2025-01-17T16:45:00Z'
                },
                'recommendations': [
                    'Consider reaching out to Sarah Johnson (your connection) for a referral',
                    'Follow up with a personalized message in 2 days'
                ]
            }
            
            return status
            
        except Exception as e:
            print(f"❌ Application tracking failed: {e}")
            return {'status': 'unknown', 'error': str(e)}

class JobrightWorkflow:
    """
    Complete workflow combining Jobright.ai's strengths with your AI system
    """
    
    def __init__(self):
        self.jobright = JobrightIntegration()
        # Import your existing AI system
        from ai.crewai_career_agents import CrewAICareerSystem
        from ai.vector_career_db import VectorCareerDatabase
        self.crew_ai = CrewAICareerSystem()
        self.vector_db = VectorCareerDatabase()
    
    async def intelligent_job_search_workflow(self, user_profile: Dict[str, Any], preferences: Dict[str, Any]) -> Dict[str, Any]:
        """
        Complete workflow: Jobright.ai job discovery + Your AI intelligence + Better resume tools
        """
        
        # 1. Use Jobright.ai for job discovery (their strength)
        print("🔍 Step 1: Discovering jobs with Jobright.ai...")
        job_matches = await self.jobright.find_job_matches(user_profile, preferences)
        
        # 2. Use your AI system for intelligent analysis
        print("🤖 Step 2: Analyzing jobs with your CrewAI system...")
        analyzed_jobs = []
        for job in job_matches:
            # Your AI decides if worth pursuing
            crew_analysis = await self.crew_ai.analyze_career_opportunity({
                'job_description': job.description,
                'title': job.title,
                'company': job.company,
                'requirements': job.requirements
            }, user_profile)
            
            # Check against your historical data
            similar_apps = self.vector_db.semantic_job_search(job.description, n_results=3)
            
            analyzed_jobs.append({
                'job': job,
                'crew_analysis': crew_analysis,
                'historical_patterns': similar_apps,
                'recommendation': crew_analysis.get('recommendation', 'review')
            })
        
        # 3. For recommended jobs, get networking insights
        print("🤝 Step 3: Finding insider connections...")
        priority_jobs = [aj for aj in analyzed_jobs if aj['recommendation'] == 'apply']
        
        for job_analysis in priority_jobs:
            connections = await self.jobright.get_insider_connections(
                job_analysis['job'], 
                user_profile.get('linkedin', {})
            )
            job_analysis['networking_opportunities'] = connections
        
        return {
            'total_jobs_found': len(job_matches),
            'jobs_analyzed': len(analyzed_jobs),
            'priority_applications': len(priority_jobs),
            'detailed_analysis': analyzed_jobs,
            'next_steps': [
                f"Apply to {len(priority_jobs)} high-priority positions",
                "Leverage networking connections for referrals",
                "Set up application tracking and follow-ups"
            ]
        }

# Example usage combining Jobright.ai strengths with your AI
async def demo_hybrid_approach():
    """Demonstrate the hybrid approach avoiding Jobright.ai's weak resume features"""
    
    workflow = JobrightWorkflow()
    
    user_profile = {
        'skills': ['Python', 'Machine Learning', 'AWS', 'Data Engineering'],
        'experience_years': 6,
        'current_role': 'Senior Data Scientist',
        'industry': 'Technology'
    }
    
    preferences = {
        'locations': ['San Francisco', 'Remote'],
        'salary_min': 150000,
        'job_types': ['full-time'],
        'match_threshold': 0.8
    }
    
    results = await workflow.intelligent_job_search_workflow(user_profile, preferences)
    
    print("\n🎯 HYBRID APPROACH RESULTS:")
    print(f"✅ Jobs discovered: {results['total_jobs_found']} (Jobright.ai strength)")
    print(f"🤖 AI analysis completed: {results['jobs_analyzed']} (Your AI intelligence)")
    print(f"🚀 Priority applications: {results['priority_applications']}")
    print("\n📋 Next Steps:")
    for step in results['next_steps']:
        print(f"   • {step}")

if __name__ == "__main__":
    asyncio.run(demo_hybrid_approach())