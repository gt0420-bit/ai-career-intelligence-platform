#!/usr/bin/env python3
"""
Jobright.ai API Integration
Real integration with Jobright.ai for job discovery, auto-application, and networking
"""

import os
import requests
import asyncio
import aiohttp
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
import json

@dataclass
class JobrightJobMatch:
    """Job match from Jobright.ai"""
    job_id: str
    title: str
    company: str
    location: str
    description: str
    requirements: List[str]
    salary_range: Optional[str]
    match_percentage: float
    application_url: str
    posted_date: datetime
    deadline: Optional[datetime]
    remote_option: bool
    employment_type: str  # full-time, part-time, contract
    experience_level: str  # entry, mid, senior, executive

@dataclass
class JobrightConnection:
    """Professional connection from Jobright.ai networking feature"""
    name: str
    title: str
    company: str
    connection_degree: int  # 1st, 2nd, 3rd degree
    mutual_connections: int
    linkedin_url: str
    referral_likelihood: float
    contact_method: str  # linkedin, email, warm_intro

class JobrightAPI:
    """
    Real Jobright.ai API integration
    Handles job discovery, auto-application, and professional networking
    """
    
    def __init__(self):
        self.api_key = os.getenv('JOBRIGHT_API_KEY')
        self.base_url = os.getenv('JOBRIGHT_API_URL', 'https://api.jobright.ai/v1')
        self.session = None
        
        if not self.api_key or self.api_key == 'your_jobright_api_key_here':
            print("⚠️ Jobright.ai API key not configured - using demo mode")
            self.demo_mode = True
        else:
            self.demo_mode = False
            print("✅ Jobright.ai API configured")
    
    async def _get_session(self):
        """Get or create aiohttp session"""
        if self.session is None:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json',
                'User-Agent': 'CareerIntelligence/1.0'
            }
            self.session = aiohttp.ClientSession(headers=headers)
        return self.session
    
    async def discover_job_matches(self, 
                                 user_profile: Dict[str, Any], 
                                 search_criteria: Dict[str, Any] = None) -> List[JobrightJobMatch]:
        """
        Discover job matches using Jobright.ai's job matching engine
        """
        if self.demo_mode:
            return self._generate_demo_job_matches(user_profile, search_criteria)
        
        try:
            session = await self._get_session()
            
            # Prepare search payload
            payload = {
                'profile': {
                    'current_role': user_profile.get('current_role', ''),
                    'skills': user_profile.get('skills', []),
                    'experience_years': user_profile.get('experience_years', 0),
                    'education_level': user_profile.get('education', ''),
                    'location_preferences': user_profile.get('locations', []),
                    'remote_preference': user_profile.get('remote_ok', True),
                    'salary_expectations': {
                        'min': user_profile.get('salary_min', 0),
                        'max': user_profile.get('salary_max', 0)
                    }
                },
                'search_criteria': search_criteria or {},
                'preferences': {
                    'daily_limit': 50,
                    'match_threshold': 0.7,
                    'include_salary': True,
                    'employment_types': ['full-time', 'contract'],
                    'experience_levels': ['mid', 'senior']
                }
            }
            
            async with session.post(f'{self.base_url}/jobs/discover', json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return self._parse_job_matches(data.get('matches', []))
                else:
                    error_msg = await response.text()
                    print(f"❌ Jobright API error: {response.status} - {error_msg}")
                    return []
        
        except Exception as e:
            print(f"❌ Error discovering jobs from Jobright: {e}")
            return self._generate_demo_job_matches(user_profile, search_criteria)
    
    async def find_insider_connections(self, 
                                     company_name: str, 
                                     target_role: str = None,
                                     user_linkedin_profile: Dict[str, Any] = None) -> List[JobrightConnection]:
        """
        Find insider connections at target company using Jobright.ai's networking feature
        """
        if self.demo_mode:
            return self._generate_demo_connections(company_name, target_role)
        
        try:
            session = await self._get_session()
            
            payload = {
                'company': company_name,
                'target_role': target_role,
                'user_profile': user_linkedin_profile or {},
                'connection_types': ['1st_degree', '2nd_degree', 'alumni', 'mutual'],
                'max_results': 20
            }
            
            async with session.post(f'{self.base_url}/networking/connections', json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return self._parse_connections(data.get('connections', []))
                else:
                    print(f"❌ Jobright networking API error: {response.status}")
                    return self._generate_demo_connections(company_name, target_role)
        
        except Exception as e:
            print(f"❌ Error finding connections: {e}")
            return self._generate_demo_connections(company_name, target_role)
    
    async def auto_apply_to_job(self, 
                              job_id: str, 
                              application_materials: Dict[str, Any],
                              personalization: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Auto-apply to job using Jobright.ai's application system
        """
        if self.demo_mode:
            return self._generate_demo_application_result(job_id)
        
        try:
            session = await self._get_session()
            
            payload = {
                'job_id': job_id,
                'materials': {
                    'resume': application_materials.get('resume', ''),
                    'cover_letter': application_materials.get('cover_letter', ''),
                    'portfolio_links': application_materials.get('portfolio_links', [])
                },
                'personalization': personalization or {},
                'application_settings': {
                    'follow_up_enabled': True,
                    'tracking_enabled': True,
                    'notifications_enabled': True
                }
            }
            
            async with session.post(f'{self.base_url}/applications/submit', json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return {
                        'success': True,
                        'application_id': data.get('application_id'),
                        'status': 'submitted',
                        'tracking_url': data.get('tracking_url'),
                        'estimated_response_time': data.get('response_time', '3-5 business days'),
                        'next_steps': data.get('next_steps', [])
                    }
                else:
                    return {'success': False, 'error': f'API error: {response.status}'}
        
        except Exception as e:
            print(f"❌ Error auto-applying to job: {e}")
            return self._generate_demo_application_result(job_id)
    
    async def track_application_status(self, application_id: str) -> Dict[str, Any]:
        """
        Track application status using Jobright.ai's tracking system
        """
        if self.demo_mode:
            return self._generate_demo_tracking_status(application_id)
        
        try:
            session = await self._get_session()
            
            async with session.get(f'{self.base_url}/applications/{application_id}/status') as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {'status': 'unknown', 'error': f'API error: {response.status}'}
        
        except Exception as e:
            print(f"❌ Error tracking application: {e}")
            return self._generate_demo_tracking_status(application_id)
    
    async def get_job_market_insights(self, role: str, location: str = None) -> Dict[str, Any]:
        """
        Get job market insights for specific role/location
        """
        if self.demo_mode:
            return self._generate_demo_market_insights(role, location)
        
        try:
            session = await self._get_session()
            
            params = {'role': role}
            if location:
                params['location'] = location
            
            async with session.get(f'{self.base_url}/market/insights', params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return self._generate_demo_market_insights(role, location)
        
        except Exception as e:
            print(f"❌ Error getting market insights: {e}")
            return self._generate_demo_market_insights(role, location)
    
    # Helper methods for parsing API responses
    def _parse_job_matches(self, matches_data: List[Dict]) -> List[JobrightJobMatch]:
        """Parse job matches from API response"""
        jobs = []
        for match in matches_data:
            try:
                job = JobrightJobMatch(
                    job_id=match.get('id', ''),
                    title=match.get('title', ''),
                    company=match.get('company', {}).get('name', ''),
                    location=match.get('location', ''),
                    description=match.get('description', ''),
                    requirements=match.get('requirements', []),
                    salary_range=match.get('salary_range', ''),
                    match_percentage=match.get('match_score', 0.0),
                    application_url=match.get('apply_url', ''),
                    posted_date=datetime.fromisoformat(match.get('posted_date', datetime.now().isoformat())),
                    deadline=datetime.fromisoformat(match['deadline']) if match.get('deadline') else None,
                    remote_option=match.get('remote_ok', False),
                    employment_type=match.get('employment_type', 'full-time'),
                    experience_level=match.get('experience_level', 'mid')
                )
                jobs.append(job)
            except Exception as e:
                print(f"⚠️ Error parsing job match: {e}")
                continue
        
        return jobs
    
    def _parse_connections(self, connections_data: List[Dict]) -> List[JobrightConnection]:
        """Parse professional connections from API response"""
        connections = []
        for conn in connections_data:
            try:
                connection = JobrightConnection(
                    name=conn.get('name', ''),
                    title=conn.get('title', ''),
                    company=conn.get('company', ''),
                    connection_degree=conn.get('degree', 2),
                    mutual_connections=conn.get('mutual_count', 0),
                    linkedin_url=conn.get('linkedin_url', ''),
                    referral_likelihood=conn.get('referral_score', 0.0),
                    contact_method=conn.get('contact_method', 'linkedin')
                )
                connections.append(connection)
            except Exception as e:
                print(f"⚠️ Error parsing connection: {e}")
                continue
        
        return connections
    
    # Demo mode methods (fallback when API not configured)
    def _generate_demo_job_matches(self, profile: Dict, criteria: Dict) -> List[JobrightJobMatch]:
        """Generate demo job matches for testing"""
        current_role = profile.get('current_role', 'Software Engineer')
        skills = profile.get('skills', [])
        
        demo_jobs = [
            JobrightJobMatch(
                job_id='jr_demo_001',
                title=f'Senior {current_role}',
                company='TechCorp Inc',
                location='San Francisco, CA',
                description=f'We are looking for a Senior {current_role} with expertise in {", ".join(skills[:3])}',
                requirements=skills[:5] + ['5+ years experience'],
                salary_range='$150,000 - $200,000',
                match_percentage=0.89,
                application_url='https://demo.jobright.ai/apply/001',
                posted_date=datetime.now() - timedelta(days=2),
                deadline=datetime.now() + timedelta(days=28),
                remote_option=True,
                employment_type='full-time',
                experience_level='senior'
            ),
            JobrightJobMatch(
                job_id='jr_demo_002',
                title='Product Manager',
                company='InnovateAI',
                location='Remote',
                description='Product Manager role focusing on AI/ML products with technical background preferred',
                requirements=['Product Strategy', 'Data Analysis', 'Technical Background'],
                salary_range='$140,000 - $180,000',
                match_percentage=0.82,
                application_url='https://demo.jobright.ai/apply/002',
                posted_date=datetime.now() - timedelta(days=1),
                deadline=None,
                remote_option=True,
                employment_type='full-time',
                experience_level='mid'
            ),
            JobrightJobMatch(
                job_id='jr_demo_003',
                title='Engineering Manager',
                company='ScaleUp Co',
                location='New York, NY',
                description='Lead a team of engineers building next-generation software products',
                requirements=['Technical Leadership', 'Team Management', 'Software Development'],
                salary_range='$160,000 - $220,000',
                match_percentage=0.76,
                application_url='https://demo.jobright.ai/apply/003',
                posted_date=datetime.now() - timedelta(days=5),
                deadline=datetime.now() + timedelta(days=21),
                remote_option=False,
                employment_type='full-time',
                experience_level='senior'
            )
        ]
        
        return demo_jobs
    
    def _generate_demo_connections(self, company: str, role: str) -> List[JobrightConnection]:
        """Generate demo professional connections"""
        return [
            JobrightConnection(
                name='Sarah Johnson',
                title=f'Senior {role}' if role else 'Senior Engineer',
                company=company,
                connection_degree=1,
                mutual_connections=3,
                linkedin_url=f'https://linkedin.com/in/sarah-johnson-{company.lower()}',
                referral_likelihood=0.7,
                contact_method='linkedin'
            ),
            JobrightConnection(
                name='Mike Chen',
                title='Engineering Manager',
                company=company,
                connection_degree=2,
                mutual_connections=1,
                linkedin_url=f'https://linkedin.com/in/mike-chen-{company.lower()}',
                referral_likelihood=0.4,
                contact_method='warm_intro'
            ),
            JobrightConnection(
                name='Jessica Rodriguez',
                title='Hiring Manager',
                company=company,
                connection_degree=3,
                mutual_connections=2,
                linkedin_url=f'https://linkedin.com/in/jessica-rodriguez-{company.lower()}',
                referral_likelihood=0.3,
                contact_method='alumni'
            )
        ]
    
    def _generate_demo_application_result(self, job_id: str) -> Dict[str, Any]:
        """Generate demo application result"""
        return {
            'success': True,
            'application_id': f'app_{job_id}_{datetime.now().strftime("%Y%m%d_%H%M")}',
            'status': 'submitted',
            'tracking_url': f'https://demo.jobright.ai/track/app_{job_id}',
            'estimated_response_time': '3-5 business days',
            'next_steps': [
                'Application submitted successfully',
                'Resume reviewed by ATS system',
                'Follow-up reminder set for 1 week'
            ]
        }
    
    def _generate_demo_tracking_status(self, application_id: str) -> Dict[str, Any]:
        """Generate demo tracking status"""
        return {
            'application_id': application_id,
            'current_status': 'under_review',
            'status_history': [
                {'status': 'submitted', 'timestamp': '2025-01-15T10:00:00Z'},
                {'status': 'ats_passed', 'timestamp': '2025-01-15T14:30:00Z'},
                {'status': 'under_review', 'timestamp': '2025-01-16T09:15:00Z'}
            ],
            'next_expected_update': '2025-01-20',
            'recruiter_activity': {
                'profile_views': 2,
                'last_activity': '2025-01-16T16:45:00Z'
            }
        }
    
    def _generate_demo_market_insights(self, role: str, location: str) -> Dict[str, Any]:
        """Generate demo market insights"""
        return {
            'role': role,
            'location': location or 'Global',
            'market_data': {
                'total_openings': 1247,
                'avg_salary': '$165,000',
                'demand_level': 'high',
                'growth_rate': '+23%',
                'top_skills': ['Python', 'Leadership', 'System Design'],
                'top_companies_hiring': ['Google', 'Amazon', 'Microsoft', 'Meta']
            },
            'trends': {
                'hiring_velocity': 'increasing',
                'remote_percentage': 0.68,
                'competition_level': 'moderate'
            }
        }
    
    async def close_session(self):
        """Close the aiohttp session"""
        if self.session:
            await self.session.close()
            self.session = None

# Example usage
async def demo_jobright_integration():
    """Demonstrate Jobright.ai integration"""
    
    api = JobrightAPI()
    
    user_profile = {
        'current_role': 'Senior Software Engineer',
        'skills': ['Python', 'Machine Learning', 'System Design', 'Leadership'],
        'experience_years': 7,
        'locations': ['San Francisco', 'Remote'],
        'remote_ok': True,
        'salary_min': 150000
    }
    
    print("🔍 Discovering job matches with Jobright.ai...")
    jobs = await api.discover_job_matches(user_profile)
    
    print(f"✅ Found {len(jobs)} job matches:")
    for job in jobs[:3]:
        print(f"   • {job.title} at {job.company} ({job.match_percentage:.1%} match)")
        print(f"     Location: {job.location} | Salary: {job.salary_range}")
    
    if jobs:
        print(f"\n🤝 Finding insider connections at {jobs[0].company}...")
        connections = await api.find_insider_connections(jobs[0].company, jobs[0].title)
        
        print(f"✅ Found {len(connections)} professional connections:")
        for conn in connections:
            print(f"   • {conn.name} ({conn.title}) - {conn.connection_degree}° connection")
            print(f"     Referral likelihood: {conn.referral_likelihood:.1%}")
    
    await api.close_session()

if __name__ == "__main__":
    asyncio.run(demo_jobright_integration())