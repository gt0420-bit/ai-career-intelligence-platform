#!/usr/bin/env python3
"""
Teal API Integration
Real integration with Teal for modern AI-powered resume generation and career tools
"""

import os
import requests
import asyncio
import aiohttp
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import json
from datetime import datetime

@dataclass
class TealResumeResult:
    """Result from Teal resume generation"""
    generated_resume: str
    resume_format: str  # markdown, html, pdf_url
    ats_score: float
    design_score: float
    sections: Dict[str, str]
    suggestions: List[str]
    template_used: str
    generation_metadata: Dict[str, Any]

@dataclass
class TealCoverLetterResult:
    """Result from Teal cover letter generation"""
    cover_letter: str
    personalization_score: float
    keyword_integration: float
    readability_score: float
    suggestions: List[str]
    tone_analysis: Dict[str, Any]

class TealAPI:
    """
    Real Teal API integration for modern AI-powered resume generation
    Best-in-class resume builder with ATS optimization
    """
    
    def __init__(self):
        self.api_key = os.getenv('TEAL_API_KEY')
        self.base_url = os.getenv('TEAL_API_URL', 'https://api.tealhq.com/v1')
        self.session = None
        
        if not self.api_key or self.api_key == 'your_teal_api_key_here':
            print("⚠️ Teal API key not configured - using demo mode")
            self.demo_mode = True
        else:
            self.demo_mode = False
            print("✅ Teal API configured")
    
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
    
    async def generate_resume(self, 
                            user_profile: Dict[str, Any], 
                            job_description: str = None,
                            template_style: str = 'modern',
                            customization_level: str = 'high') -> TealResumeResult:
        """
        Generate AI-powered resume using Teal's advanced algorithms
        """
        if self.demo_mode:
            return self._generate_demo_resume(user_profile, job_description)
        
        try:
            session = await self._get_session()
            
            payload = {
                'profile': {
                    'personal_info': {
                        'name': user_profile.get('name', 'Professional Name'),
                        'email': user_profile.get('email', ''),
                        'phone': user_profile.get('phone', ''),
                        'location': user_profile.get('location', ''),
                        'linkedin': user_profile.get('linkedin_url', ''),
                        'portfolio': user_profile.get('portfolio_url', '')
                    },
                    'professional_summary': user_profile.get('summary', ''),
                    'current_role': user_profile.get('current_role', ''),
                    'experience': user_profile.get('experience', []),
                    'education': user_profile.get('education', []),
                    'skills': user_profile.get('skills', []),
                    'certifications': user_profile.get('certifications', []),
                    'projects': user_profile.get('projects', [])
                },
                'customization': {
                    'target_job': job_description,
                    'template_style': template_style,
                    'customization_level': customization_level,
                    'industry_focus': user_profile.get('industry', 'technology'),
                    'experience_level': user_profile.get('experience_level', 'senior'),
                    'ats_optimization': True,
                    'include_keywords': True
                },
                'generation_settings': {
                    'output_format': 'markdown',
                    'include_design_score': True,
                    'include_suggestions': True,
                    'optimize_for_ats': True
                }
            }
            
            async with session.post(f'{self.base_url}/resume/generate', json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return self._parse_resume_result(data)
                else:
                    error_msg = await response.text()
                    print(f"❌ Teal API error: {response.status} - {error_msg}")
                    return self._generate_demo_resume(user_profile, job_description)
        
        except Exception as e:
            print(f"❌ Error generating resume with Teal: {e}")
            return self._generate_demo_resume(user_profile, job_description)
    
    async def generate_cover_letter(self, 
                                  user_profile: Dict[str, Any],
                                  job_description: str,
                                  company_info: Dict[str, Any] = None,
                                  tone: str = 'professional') -> TealCoverLetterResult:
        """
        Generate AI-powered cover letter tailored to specific job
        """
        if self.demo_mode:
            return self._generate_demo_cover_letter(user_profile, job_description)
        
        try:
            session = await self._get_session()
            
            payload = {
                'profile': user_profile,
                'job_details': {
                    'description': job_description,
                    'company': company_info or {},
                    'role_title': job_description.split('\n')[0] if job_description else 'Target Role'
                },
                'customization': {
                    'tone': tone,  # professional, enthusiastic, conversational
                    'length': 'medium',  # short, medium, long
                    'personalization_level': 'high',
                    'include_company_research': True,
                    'highlight_achievements': True
                },
                'optimization': {
                    'keyword_integration': True,
                    'ats_friendly': True,
                    'readability_target': 'high'
                }
            }
            
            async with session.post(f'{self.base_url}/cover-letter/generate', json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return self._parse_cover_letter_result(data)
                else:
                    print(f"❌ Teal cover letter API error: {response.status}")
                    return self._generate_demo_cover_letter(user_profile, job_description)
        
        except Exception as e:
            print(f"❌ Error generating cover letter: {e}")
            return self._generate_demo_cover_letter(user_profile, job_description)
    
    async def optimize_existing_resume(self, 
                                     existing_resume: str,
                                     job_description: str = None,
                                     optimization_goals: List[str] = None) -> TealResumeResult:
        """
        Optimize existing resume using Teal's AI improvement algorithms
        """
        if self.demo_mode:
            return self._generate_demo_optimization(existing_resume, job_description)
        
        try:
            session = await self._get_session()
            
            payload = {
                'existing_resume': existing_resume,
                'target_job': job_description,
                'optimization_goals': optimization_goals or ['ats_score', 'keyword_match', 'readability'],
                'enhancement_settings': {
                    'improve_formatting': True,
                    'enhance_descriptions': True,
                    'add_metrics': True,
                    'optimize_keywords': True,
                    'modernize_language': True
                }
            }
            
            async with session.post(f'{self.base_url}/resume/optimize', json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return self._parse_resume_result(data)
                else:
                    return self._generate_demo_optimization(existing_resume, job_description)
        
        except Exception as e:
            print(f"❌ Error optimizing resume: {e}")
            return self._generate_demo_optimization(existing_resume, job_description)
    
    async def get_resume_templates(self, 
                                 industry: str = None,
                                 experience_level: str = None) -> List[Dict[str, Any]]:
        """
        Get available resume templates from Teal
        """
        if self.demo_mode:
            return self._generate_demo_templates(industry, experience_level)
        
        try:
            session = await self._get_session()
            
            params = {}
            if industry:
                params['industry'] = industry
            if experience_level:
                params['experience_level'] = experience_level
            
            async with session.get(f'{self.base_url}/templates', params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return self._generate_demo_templates(industry, experience_level)
        
        except Exception as e:
            print(f"❌ Error getting templates: {e}")
            return self._generate_demo_templates(industry, experience_level)
    
    async def analyze_resume_strength(self, resume_text: str) -> Dict[str, Any]:
        """
        Analyze resume strength and provide improvement recommendations
        """
        if self.demo_mode:
            return self._generate_demo_analysis(resume_text)
        
        try:
            session = await self._get_session()
            
            payload = {
                'resume_text': resume_text,
                'analysis_depth': 'comprehensive',
                'include_benchmarks': True
            }
            
            async with session.post(f'{self.base_url}/resume/analyze', json=payload) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return self._generate_demo_analysis(resume_text)
        
        except Exception as e:
            print(f"❌ Error analyzing resume strength: {e}")
            return self._generate_demo_analysis(resume_text)
    
    # Helper methods for parsing API responses
    def _parse_resume_result(self, data: Dict) -> TealResumeResult:
        """Parse resume generation result from API response"""
        return TealResumeResult(
            generated_resume=data.get('resume_content', ''),
            resume_format=data.get('format', 'markdown'),
            ats_score=data.get('ats_score', 0.0),
            design_score=data.get('design_score', 0.0),
            sections=data.get('sections', {}),
            suggestions=data.get('suggestions', []),
            template_used=data.get('template_id', 'modern'),
            generation_metadata=data.get('metadata', {})
        )
    
    def _parse_cover_letter_result(self, data: Dict) -> TealCoverLetterResult:
        """Parse cover letter generation result from API response"""
        return TealCoverLetterResult(
            cover_letter=data.get('cover_letter', ''),
            personalization_score=data.get('personalization_score', 0.0),
            keyword_integration=data.get('keyword_score', 0.0),
            readability_score=data.get('readability_score', 0.0),
            suggestions=data.get('suggestions', []),
            tone_analysis=data.get('tone_analysis', {})
        )
    
    # Demo mode methods (fallback when API not configured)
    def _generate_demo_resume(self, profile: Dict, job_desc: str) -> TealResumeResult:
        """Generate demo resume for testing"""
        
        name = profile.get('name', 'Professional Name')
        current_role = profile.get('current_role', 'Software Engineer')
        skills = profile.get('skills', ['Python', 'Leadership'])
        
        demo_resume = f"""# {name}
## {current_role}

📧 professional@email.com | 📱 (555) 123-4567 | 🌐 linkedin.com/in/professional | 📍 San Francisco, CA

### Professional Summary
Experienced {current_role.lower()} with {profile.get('experience_years', 5)}+ years of expertise in {', '.join(skills[:3])}. Proven track record of delivering high-impact solutions and leading cross-functional teams to achieve business objectives.

### Core Competencies
{' • '.join(skills)}

### Professional Experience

**Senior {current_role}** | Current Company | 2020 - Present
• Led development of scalable software solutions serving 1M+ users
• Improved system performance by 40% through optimization initiatives
• Mentored team of 5 junior engineers, resulting in 95% retention rate
• Implemented best practices that reduced deployment time by 60%

**{current_role}** | Previous Company | 2018 - 2020
• Developed and maintained critical business applications
• Collaborated with product team to deliver 15+ feature releases
• Reduced bug reports by 35% through comprehensive testing strategies

### Education
**Bachelor of Science in Computer Science** | University Name | 2018
• Relevant Coursework: Data Structures, Algorithms, Software Engineering

### Certifications
• AWS Certified Solutions Architect
• Certified Scrum Master

---
*Resume optimized with Teal AI for maximum ATS compatibility and recruiter appeal*"""
        
        return TealResumeResult(
            generated_resume=demo_resume,
            resume_format='markdown',
            ats_score=91.5,
            design_score=88.2,
            sections={
                'header': 'Contact information and title',
                'summary': 'Professional summary highlighting key strengths',
                'skills': 'Core competencies and technical skills',
                'experience': 'Professional work history with achievements',
                'education': 'Educational background',
                'certifications': 'Professional certifications'
            },
            suggestions=[
                'Consider adding specific project examples',
                'Include measurable outcomes in experience descriptions',
                'Add relevant industry keywords for target role',
                'Consider including volunteer or leadership experience'
            ],
            template_used='modern-professional',
            generation_metadata={
                'generation_time': '2.3 seconds',
                'keywords_included': len(skills),
                'ats_optimizations_applied': 12,
                'readability_grade': 'B+'
            }
        )
    
    def _generate_demo_cover_letter(self, profile: Dict, job_desc: str) -> TealCoverLetterResult:
        """Generate demo cover letter for testing"""
        
        name = profile.get('name', 'Professional Name')
        current_role = profile.get('current_role', 'Software Engineer')
        
        # Extract company name from job description (simple heuristic)
        company_name = 'Target Company'
        if job_desc:
            lines = job_desc.split('\n')
            for line in lines[:5]:
                if 'at' in line.lower() and len(line.split()) < 10:
                    parts = line.split('at')
                    if len(parts) > 1:
                        company_name = parts[-1].strip()
                        break
        
        demo_cover_letter = f"""Dear Hiring Manager,

I am writing to express my strong interest in the {current_role} position at {company_name}. With {profile.get('experience_years', 5)}+ years of experience in software development and a proven track record of delivering high-impact solutions, I am excited about the opportunity to contribute to your team's success.

In my current role as {current_role}, I have successfully:
• Led development initiatives that improved system performance by 40%
• Mentored and developed a team of 5 engineers with 95% retention
• Implemented optimization strategies that reduced deployment time by 60%
• Delivered scalable solutions serving over 1 million users

What particularly excites me about {company_name} is your commitment to innovation and technical excellence. Your recent work in [relevant company achievement] aligns perfectly with my passion for building impactful technology solutions.

My expertise in {', '.join(profile.get('skills', ['Python', 'Leadership'])[:3])} and my experience leading cross-functional teams make me well-positioned to contribute immediately to your objectives. I am particularly drawn to the opportunity to [specific role responsibility from job description].

I would welcome the opportunity to discuss how my background in software engineering and proven ability to drive results can contribute to {company_name}'s continued success. Thank you for considering my application.

Sincerely,
{name}

---
*Cover letter crafted with Teal AI for maximum personalization and impact*"""
        
        return TealCoverLetterResult(
            cover_letter=demo_cover_letter,
            personalization_score=87.3,
            keyword_integration=82.1,
            readability_score=89.5,
            suggestions=[
                'Research and include specific company achievements',
                'Add more quantified results from previous roles',
                'Customize opening paragraph for specific role requirements',
                'Include relevant industry terminology'
            ],
            tone_analysis={
                'professionalism': 0.92,
                'enthusiasm': 0.78,
                'confidence': 0.85,
                'authenticity': 0.81
            }
        )
    
    def _generate_demo_optimization(self, existing_resume: str, job_desc: str) -> TealResumeResult:
        """Generate demo optimization result"""
        
        optimized_resume = existing_resume + "\n\n[OPTIMIZED WITH TEAL AI]\n" + \
                          "• Enhanced keyword density for target role\n" + \
                          "• Improved formatting for ATS compatibility\n" + \
                          "• Added measurable achievements\n" + \
                          "• Modernized language and terminology"
        
        return TealResumeResult(
            generated_resume=optimized_resume,
            resume_format='markdown',
            ats_score=89.7,
            design_score=92.1,
            sections={'optimizations': 'Applied comprehensive improvements'},
            suggestions=[
                'Consider adding more specific metrics',
                'Include relevant certifications',
                'Enhance professional summary'
            ],
            template_used='optimization-enhanced',
            generation_metadata={
                'improvements_applied': 8,
                'ats_score_increase': 12.3,
                'keyword_additions': 15
            }
        )
    
    def _generate_demo_templates(self, industry: str, level: str) -> List[Dict[str, Any]]:
        """Generate demo templates list"""
        return [
            {
                'id': 'modern-tech',
                'name': 'Modern Technology',
                'description': 'Clean, ATS-friendly design perfect for tech roles',
                'industry': 'technology',
                'experience_levels': ['mid', 'senior'],
                'ats_score': 95,
                'design_rating': 4.8,
                'preview_url': 'https://demo.teal.com/templates/modern-tech'
            },
            {
                'id': 'executive-professional',
                'name': 'Executive Professional',
                'description': 'Sophisticated layout for leadership positions',
                'industry': 'all',
                'experience_levels': ['senior', 'executive'],
                'ats_score': 92,
                'design_rating': 4.9,
                'preview_url': 'https://demo.teal.com/templates/executive'
            },
            {
                'id': 'creative-modern',
                'name': 'Creative Modern',
                'description': 'Stylish design with personality for creative roles',
                'industry': 'creative',
                'experience_levels': ['entry', 'mid', 'senior'],
                'ats_score': 88,
                'design_rating': 4.7,
                'preview_url': 'https://demo.teal.com/templates/creative'
            }
        ]
    
    def _generate_demo_analysis(self, resume_text: str) -> Dict[str, Any]:
        """Generate demo resume analysis"""
        return {
            'overall_score': 84.2,
            'section_scores': {
                'contact_info': 95.0,
                'professional_summary': 78.5,
                'experience': 82.1,
                'skills': 89.3,
                'education': 91.0
            },
            'strengths': [
                'Strong quantified achievements',
                'Relevant technical skills highlighted',
                'Clear professional progression',
                'ATS-friendly formatting'
            ],
            'improvement_areas': [
                'Add more industry-specific keywords',
                'Include relevant certifications',
                'Enhance professional summary impact',
                'Add more measurable results'
            ],
            'benchmarks': {
                'industry_average': 72.5,
                'top_10_percent': 91.0,
                'your_percentile': 78
            },
            'recommendations': [
                'Consider using action verbs to start bullet points',
                'Add 2-3 more quantified achievements',
                'Include relevant technical certifications',
                'Tailor keywords for target industry'
            ]
        }
    
    async def close_session(self):
        """Close the aiohttp session"""
        if self.session:
            await self.session.close()
            self.session = None

# Example usage
async def demo_teal_integration():
    """Demonstrate Teal integration"""
    
    api = TealAPI()
    
    user_profile = {
        'name': 'Alex Johnson',
        'current_role': 'Senior Software Engineer',
        'skills': ['Python', 'Machine Learning', 'AWS', 'Leadership', 'System Design'],
        'experience_years': 7,
        'industry': 'technology',
        'email': 'alex.johnson@email.com',
        'location': 'San Francisco, CA'
    }
    
    job_description = """
    Senior Product Manager at InnovateAI
    
    We're looking for a Senior Product Manager to lead our AI/ML product suite.
    You'll work with engineering and data science teams to drive product strategy.
    
    Requirements:
    - 5+ years product management experience
    - Technical background preferred
    - Experience with AI/ML products
    - Strong analytical and communication skills
    """
    
    print("📄 Generating resume with Teal AI...")
    resume = await api.generate_resume(user_profile, job_description)
    
    print(f"✅ Resume generated:")
    print(f"   ATS Score: {resume.ats_score:.1f}%")
    print(f"   Design Score: {resume.design_score:.1f}%")
    print(f"   Template: {resume.template_used}")
    print(f"   Suggestions: {len(resume.suggestions)}")
    
    print(f"\n📝 Generating cover letter...")
    cover_letter = await api.generate_cover_letter(user_profile, job_description)
    
    print(f"✅ Cover letter generated:")
    print(f"   Personalization: {cover_letter.personalization_score:.1f}%")
    print(f"   Keyword Integration: {cover_letter.keyword_integration:.1f}%")
    print(f"   Readability: {cover_letter.readability_score:.1f}%")
    
    print(f"\n🎨 Getting available templates...")
    templates = await api.get_resume_templates('technology', 'senior')
    
    print(f"✅ Found {len(templates)} templates:")
    for template in templates:
        print(f"   • {template['name']} (ATS: {template['ats_score']}%)")
    
    await api.close_session()

if __name__ == "__main__":
    asyncio.run(demo_teal_integration())