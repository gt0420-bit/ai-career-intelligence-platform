#!/usr/bin/env python3
"""
Precision Career Intelligence API Endpoints

Advanced API endpoints for the enhanced career intelligence system that provides:
1. Precision career transition analysis
2. Strategic job discovery and alignment
3. Transferable skills intelligence
4. Company-specific insights
5. Success prediction and optimization
"""

from flask import Blueprint, request, jsonify
import asyncio
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import traceback

# Create blueprint
precision_bp = Blueprint('precision_career', __name__)

# Real integrated external API orchestrator implementation
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from ai.integrated_external_orchestrator import IntegratedExternalOrchestrator
    print("✅ Successfully imported IntegratedExternalOrchestrator")
    USE_REAL_ORCHESTRATOR = True
except ImportError as e:
    print(f"⚠️ Could not import real orchestrator: {e}")
    USE_REAL_ORCHESTRATOR = False

class MockEnhancedOrchestrator:
    """Fallback mock implementation when real orchestrator unavailable"""
    
    async def execute_precision_career_intelligence_workflow(self, user_profile: Dict[str, Any], career_goals: Dict[str, Any]) -> Dict[str, Any]:
        """Mock precision workflow execution"""
        
        # Simulate realistic processing time
        await asyncio.sleep(0.5)
        
        # Generate mock results based on input
        transition_paths = self._generate_mock_transition_paths(user_profile, career_goals)
        job_matches = self._generate_mock_job_matches(user_profile, career_goals)
        precision_applications = self._generate_mock_precision_applications(transition_paths, job_matches)
        
        return {
            'transition_intelligence': {
                'paths_analyzed': len(transition_paths),
                'strategic_transitions': [p for p in transition_paths if p['success_probability'] > 0.7],
                'top_transition': transition_paths[0] if transition_paths else None
            },
            'job_discovery': {
                'jobs_found': len(job_matches),
                'precision_aligned': len(precision_applications),
                'high_value_targets': len([app for app in precision_applications if app['strategic_value'] > 0.8])
            },
            'precision_applications': precision_applications,
            'execution_plan': self._generate_execution_plan(precision_applications),
            'competitive_advantages': [
                "Precision job-transition alignment vs random applications",
                "Best-in-class ATS optimization avoiding weak Jobright resume tools",
                "Historical pattern analysis from 266+ application dataset",
                "Multi-agent AI strategy vs single-point solutions",
                "Company insider intelligence and networking strategies",
                "Strategic timing and market condition analysis"
            ],
            'success_metrics': self._calculate_success_metrics(precision_applications)
        }
    
    def _generate_mock_transition_paths(self, profile: Dict[str, Any], goals: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate mock transition paths based on profile"""
        current_role = profile.get('current_role', 'Software Engineer')
        target_companies = goals.get('target_companies', ['Google', 'Amazon'])
        
        paths = []
        role_transitions = {
            'Software Engineer': ['Senior Software Engineer', 'Product Manager', 'Engineering Manager', 'Technical Lead'],
            'Data Scientist': ['Senior Data Scientist', 'ML Engineer', 'Data Science Manager', 'Product Manager'],
            'Product Manager': ['Senior Product Manager', 'Director of Product', 'VP Product', 'Strategy Manager']
        }
        
        target_roles = role_transitions.get(current_role, ['Senior ' + current_role])
        
        for company in target_companies[:2]:  # Limit to 2 for demo
            for role in target_roles[:2]:  # Limit to 2 for demo
                paths.append({
                    'from_role': current_role,
                    'to_role': role,
                    'target_company': company,
                    'success_probability': 0.75 + (hash(role + company) % 20) / 100,  # 0.75-0.95
                    'difficulty': 'Strategic' if 'Manager' in role else 'Natural',
                    'timeline_months': 12 if 'Manager' in role else 8,
                    'salary_change_percentage': 0.25 if 'Senior' in role else 0.15,
                    'required_skills': self._get_required_skills(role),
                    'skill_gaps': self._get_skill_gaps(current_role, role),
                    'precision_strategy': {
                        'networking_targets': [f'{role} at {company}', f'Hiring Manager for {role}'],
                        'skill_development': f'Focus on {role.lower()} specific skills',
                        'application_timing': 'Q1 2025 - Peak hiring season',
                        'success_accelerators': ['Internal referral', f'{role} certification']
                    }
                })
        
        return sorted(paths, key=lambda x: x['success_probability'], reverse=True)
    
    def _generate_mock_job_matches(self, profile: Dict[str, Any], goals: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate mock job matches"""
        matches = []
        companies = goals.get('target_companies', ['Google', 'Amazon', 'Microsoft'])
        
        for i, company in enumerate(companies):
            matches.append({
                'job_id': f'job_{i}',
                'title': f'Senior Software Engineer' if i % 2 == 0 else 'Product Manager',
                'company': company,
                'location': 'San Francisco, CA' if i % 2 == 0 else 'Remote',
                'match_percentage': 0.85 + (i % 10) / 100,
                'salary_range': '$150,000 - $200,000',
                'requirements': ['Python', 'Leadership', 'System Design'] if i % 2 == 0 else ['Product Strategy', 'Analytics', 'Stakeholder Management'],
                'description': f'Join {company} as a {matches[-1]["title"] if matches else "Software Engineer"}...'
            })
        
        return matches
    
    def _generate_mock_precision_applications(self, transitions: List[Dict], jobs: List[Dict]) -> List[Dict[str, Any]]:
        """Generate mock precision applications"""
        applications = []
        
        for i, (transition, job) in enumerate(zip(transitions[:3], jobs[:3])):
            applications.append({
                'application_id': f'app_{i}',
                'job': job,
                'transition_analysis': transition,
                'success_prediction': min(0.95, transition['success_probability'] * job['match_percentage']),
                'strategic_value': transition['success_probability'] * job['match_percentage'] * (1.0 if transition['target_company'] == job['company'] else 0.8),
                'optimized_materials': {
                    'resume': f"ATS-optimized resume for {job['title']} at {job['company']}",
                    'cover_letter': f"Tailored cover letter for {transition['from_role']} → {transition['to_role']} transition",
                    'ats_score': 0.87,
                    'optimization_summary': ['Added relevant keywords', 'Improved formatting', 'Enhanced skills section']
                },
                'ai_strategy': {
                    'application_approach': 'Emphasize transferable skills and growth mindset',
                    'key_talking_points': transition['required_skills'],
                    'differentiation_strategy': 'Highlight unique combination of technical and leadership skills',
                    'confidence': 0.9
                },
                'precision_targeting': {
                    'networking_strategy': transition['precision_strategy']['networking_targets'],
                    'application_timing': transition['precision_strategy']['application_timing'],
                    'success_accelerators': transition['precision_strategy']['success_accelerators']
                }
            })
        
        return applications
    
    def _generate_execution_plan(self, applications: List[Dict]) -> Dict[str, Any]:
        """Generate execution plan"""
        return {
            'immediate_action': {
                'timeline': 'Next 2 weeks',
                'applications': len([app for app in applications if app['success_prediction'] > 0.8]),
                'focus': 'Highest probability + highest strategic value applications',
                'actions': [
                    'Apply to top 3 strategic opportunities',
                    'Initiate networking outreach to key contacts',
                    'Begin priority skill development activities'
                ]
            },
            'success_tracking_kpis': [
                'Application-to-interview rate > 25%',
                'Interview-to-offer rate > 40%',
                'Strategic transition completion < 12 months',
                'Salary increase > 20%'
            ],
            'weekly_schedule': {
                'Week 1': ['Apply to top 2 opportunities', 'Begin networking outreach'],
                'Week 2': ['Apply to next 3 opportunities', 'Follow up on Week 1 applications'],
                'Week 3': ['Skill development focus', 'Continued networking'],
                'Week 4': ['Portfolio updates', 'Interview preparation']
            }
        }
    
    def _calculate_success_metrics(self, applications: List[Dict]) -> Dict[str, Any]:
        """Calculate success metrics"""
        if not applications:
            return {}
        
        avg_success = sum(app['success_prediction'] for app in applications) / len(applications)
        high_confidence = len([app for app in applications if app['success_prediction'] > 0.8])
        
        return {
            'average_success_prediction': f"{avg_success:.1%}",
            'high_confidence_applications': high_confidence,
            'expected_interview_rate': f"{avg_success * 1.2:.1%}",
            'time_to_success_estimate': '3-6 months'
        }
    
    def _get_required_skills(self, role: str) -> List[str]:
        """Get required skills for role"""
        skill_map = {
            'Product Manager': ['Product Strategy', 'Data Analysis', 'Stakeholder Management'],
            'Engineering Manager': ['Technical Leadership', 'Team Management', 'System Architecture'],
            'Senior Software Engineer': ['Advanced Programming', 'System Design', 'Code Review'],
            'ML Engineer': ['Machine Learning', 'MLOps', 'Production Systems']
        }
        return skill_map.get(role, ['Leadership', 'Problem Solving', 'Communication'])
    
    def _get_skill_gaps(self, current: str, target: str) -> List[str]:
        """Get skill gaps for transition"""
        gap_map = {
            ('Software Engineer', 'Product Manager'): ['Market Analysis', 'Product Strategy'],
            ('Data Scientist', 'ML Engineer'): ['MLOps', 'Production Systems'],
            ('Software Engineer', 'Engineering Manager'): ['People Management', 'Strategic Planning']
        }
        return gap_map.get((current, target), ['Industry Knowledge', 'Advanced Skills'])

# Initialize the orchestrator (use real implementation if available)
if USE_REAL_ORCHESTRATOR:
    try:
        orchestrator = IntegratedExternalOrchestrator()
        print("✅ Using real IntegratedExternalOrchestrator")
    except Exception as e:
        print(f"⚠️ Error initializing real orchestrator, falling back to mock: {e}")
        orchestrator = MockEnhancedOrchestrator()
else:
    orchestrator = MockEnhancedOrchestrator()
    print("⚠️ Using mock orchestrator")

@precision_bp.route('/analyze', methods=['POST'])
def analyze_precision_career_transition():
    """
    Analyze precision career transition opportunities
    
    Expected JSON payload:
    {
        "user_profile": {
            "current_role": "Software Engineer",
            "skills": ["Python", "Machine Learning", "Leadership"],
            "experience_years": 6,
            "industry": "Technology",
            "company": "Current Company"
        },
        "career_goals": {
            "target_companies": ["Google", "Amazon", "Microsoft"],
            "target_roles": ["Product Manager", "Engineering Manager"],
            "timeline_months": 12,
            "salary_increase_target": 0.25
        }
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        user_profile = data.get('user_profile', {})
        career_goals = data.get('career_goals', {})
        
        # Validate required fields
        if not user_profile.get('current_role'):
            return jsonify({'error': 'user_profile.current_role is required'}), 400
        
        if not career_goals.get('target_companies'):
            return jsonify({'error': 'career_goals.target_companies is required'}), 400
        
        # Execute the precision analysis workflow
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        if USE_REAL_ORCHESTRATOR and hasattr(orchestrator, 'execute_integrated_career_workflow'):
            # Use the real integrated workflow
            integrated_results = loop.run_until_complete(
                orchestrator.execute_integrated_career_workflow(
                    user_profile, career_goals
                )
            )
            # Convert integrated results to precision format
            results = {
                'transition_intelligence': {
                    'paths_analyzed': len(integrated_results.precision_analysis.get('transition_paths', [])),
                    'strategic_transitions': integrated_results.precision_analysis.get('strategic_recommendations', []),
                    'top_transition': integrated_results.precision_analysis.get('top_transition', None)
                },
                'job_discovery': {
                    'jobs_found': len(integrated_results.job_matches),
                    'precision_aligned': len(integrated_results.application_strategy.get('prioritized_applications', [])),
                    'high_value_targets': len([app for app in integrated_results.application_strategy.get('prioritized_applications', []) 
                                               if app.get('priority_score', 0) > 0.8])
                },
                'precision_applications': integrated_results.application_strategy.get('prioritized_applications', []),
                'execution_plan': integrated_results.execution_timeline,
                'competitive_advantages': integrated_results.competitive_insights,
                'success_metrics': {
                    'average_success_prediction': f"{integrated_results.success_predictions.get('overall_success_probability', 0.0):.1%}",
                    'high_confidence_applications': len([app for app in integrated_results.application_strategy.get('prioritized_applications', []) 
                                                       if app.get('priority_score', 0) > 0.8]),
                    'expected_interview_rate': "25-35%",
                    'time_to_success_estimate': integrated_results.success_predictions.get('timeline_to_success', '3-6 months')
                },
                'professional_materials': integrated_results.optimized_materials,
                'networking_intelligence': integrated_results.networking_intelligence
            }
        else:
            # Use mock workflow
            results = loop.run_until_complete(
                orchestrator.execute_precision_career_intelligence_workflow(
                    user_profile, career_goals
                )
            )
        
        loop.close()
        
        # Add metadata
        results['analysis_timestamp'] = datetime.now().isoformat()
        results['analysis_type'] = 'precision_career_transition'
        results['status'] = 'success'
        
        return jsonify(results)
    
    except Exception as e:
        print(f"❌ Error in precision career analysis: {e}")
        traceback.print_exc()
        
        return jsonify({
            'error': 'Internal server error during precision analysis',
            'details': str(e),
            'status': 'error'
        }), 500

@precision_bp.route('/transition-paths', methods=['POST'])
def get_transition_paths():
    """
    Get detailed transition paths analysis
    """
    try:
        data = request.get_json()
        user_profile = data.get('user_profile', {})
        preferences = data.get('preferences', {})
        
        # Mock transition paths data
        paths = [
            {
                'id': 'path_1',
                'from_role': user_profile.get('current_role', 'Software Engineer'),
                'to_role': 'Product Manager',
                'target_company': 'Google',
                'success_probability': 0.84,
                'difficulty': 'Strategic',
                'timeline_months': 14,
                'salary_change': '+28%',
                'transferable_skills': ['Technical Knowledge', 'Problem Solving', 'Data Analysis'],
                'skill_gaps': ['Market Analysis', 'Stakeholder Management'],
                'networking_strategy': 'Connect with 3 Google PMs who made similar transition',
                'success_factors': ['Internal referral', 'Technical PM certification', 'Product demo project']
            },
            {
                'id': 'path_2', 
                'from_role': user_profile.get('current_role', 'Software Engineer'),
                'to_role': 'Engineering Manager',
                'target_company': 'Amazon',
                'success_probability': 0.78,
                'difficulty': 'Natural',
                'timeline_months': 10,
                'salary_change': '+22%',
                'transferable_skills': ['Technical Leadership', 'System Design', 'Team Collaboration'],
                'skill_gaps': ['People Management', 'Strategic Planning'],
                'networking_strategy': 'Connect with Amazon Engineering Directors',
                'success_factors': ['Leadership experience', 'Management training', 'Team lead role']
            }
        ]
        
        return jsonify({
            'transition_paths': paths,
            'total_paths': len(paths),
            'recommended_path': paths[0],
            'analysis_timestamp': datetime.now().isoformat(),
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': 'Failed to analyze transition paths',
            'details': str(e),
            'status': 'error'
        }), 500

@precision_bp.route('/transferable-skills', methods=['POST'])
def analyze_transferable_skills():
    """
    Analyze transferable skills with market intelligence
    """
    try:
        data = request.get_json()
        current_skills = data.get('skills', [])
        target_role = data.get('target_role', '')
        
        # Mock transferable skills analysis
        skills_analysis = []
        
        skill_market_data = {
            'Python': {'demand': 0.92, 'growth': 0.15, 'transferability': 'Universal'},
            'Machine Learning': {'demand': 0.94, 'growth': 0.23, 'transferability': 'Industry-wide'},
            'Leadership': {'demand': 0.88, 'growth': 0.12, 'transferability': 'Universal'},
            'System Design': {'demand': 0.86, 'growth': 0.18, 'transferability': 'Industry-wide'}
        }
        
        for skill in current_skills:
            if skill in skill_market_data:
                data = skill_market_data[skill]
                skills_analysis.append({
                    'skill': skill,
                    'market_demand': data['demand'],
                    'growth_rate': data['growth'],
                    'transferability': data['transferability'],
                    'strategic_value': data['demand'] * (1 + data['growth']),
                    'target_role_relevance': 0.9 if skill in ['Leadership', 'Python'] else 0.7
                })
        
        return jsonify({
            'skills_analysis': skills_analysis,
            'top_transferable_skills': sorted(skills_analysis, key=lambda x: x['strategic_value'], reverse=True)[:3],
            'market_insights': {
                'hot_skills': ['Machine Learning', 'Python', 'Leadership'],
                'emerging_skills': ['MLOps', 'Product Strategy', 'Data Analysis']
            },
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': 'Failed to analyze transferable skills',
            'details': str(e),
            'status': 'error'
        }), 500

@precision_bp.route('/company-insights/<company_name>', methods=['GET'])
def get_company_insights(company_name):
    """
    Get company-specific hiring insights and intelligence
    """
    try:
        # Mock company insights
        company_data = {
            'Google': {
                'hiring_trends': {'ml_engineers': 'very_high_demand', 'product_managers': 'high_demand'},
                'preferred_transitions': {'engineer_to_pm': 0.76, 'data_scientist_to_research': 0.84},
                'culture_insights': ['Technical depth valued', 'Innovation focus', 'Data-driven decisions'],
                'interview_process': {'rounds': 5, 'focus': 'technical + behavioral', 'timeline': '4-6 weeks'},
                'success_factors': ['Technical expertise', 'Growth mindset', 'Collaborative approach']
            },
            'Amazon': {
                'hiring_trends': {'aws_specialists': 'very_high_demand', 'operations_managers': 'steady_demand'},
                'preferred_transitions': {'consultant_to_pm': 0.71, 'engineer_to_principal': 0.63},
                'culture_insights': ['Customer obsession', 'Ownership', 'Bias for action'],
                'interview_process': {'rounds': 4, 'focus': 'leadership principles', 'timeline': '3-4 weeks'},
                'success_factors': ['Results orientation', 'Customer focus', 'Innovation']
            }
        }
        
        insights = company_data.get(company_name, {
            'hiring_trends': {'general': 'moderate_demand'},
            'culture_insights': ['Professional growth', 'Team collaboration'],
            'success_factors': ['Strong performance', 'Cultural fit']
        })
        
        return jsonify({
            'company': company_name,
            'insights': insights,
            'last_updated': datetime.now().isoformat(),
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': f'Failed to get insights for {company_name}',
            'details': str(e),
            'status': 'error'
        }), 500

@precision_bp.route('/application-strategy', methods=['POST'])
def create_application_strategy():
    """
    Create precision application strategy for specific job-transition combination
    """
    try:
        data = request.get_json()
        job = data.get('job', {})
        transition = data.get('transition', {})
        user_profile = data.get('user_profile', {})
        
        # Mock application strategy creation
        strategy = {
            'application_approach': f'Position as {transition.get("from_role", "current role")} transitioning to {transition.get("to_role", "target role")}',
            'resume_optimization': {
                'key_sections': ['Skills alignment', 'Transferable experience', 'Growth trajectory'],
                'keywords_to_include': job.get('requirements', []),
                'experience_positioning': 'Emphasize leadership and technical depth'
            },
            'cover_letter_strategy': {
                'opening': f'Express genuine interest in {job.get("company", "company")} and {job.get("title", "role")}',
                'body': 'Connect current experience to target role requirements',
                'closing': 'Request informational interview or coffee chat'
            },
            'networking_approach': {
                'target_connections': [f'{job.get("title", "role")} at {job.get("company", "company")}', 'Hiring manager', 'Team members'],
                'outreach_message': f'Seeking insights on transitioning from {transition.get("from_role", "")} to {transition.get("to_role", "")}',
                'follow_up_timeline': ['1 week', '2 weeks', '1 month']
            },
            'interview_preparation': {
                'behavioral_focus': ['Career transition motivation', 'Transferable skills examples', 'Growth mindset'],
                'technical_preparation': job.get('requirements', []),
                'questions_to_ask': ['Team structure', 'Growth opportunities', 'Success metrics']
            },
            'timeline': {
                'preparation': '1-2 weeks',
                'application_submission': 'Week 2',
                'networking_outreach': 'Week 1-3',
                'follow_up_schedule': ['1 week', '2 weeks', '1 month']
            }
        }
        
        return jsonify({
            'application_strategy': strategy,
            'success_probability': min(0.95, job.get('match_percentage', 0.8) * transition.get('success_probability', 0.8)),
            'strategic_value': 'High' if strategy else 'Medium',
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': 'Failed to create application strategy',
            'details': str(e),
            'status': 'error'
        }), 500

@precision_bp.route('/integrated-demo', methods=['POST'])
def integrated_demo():
    """
    Demo endpoint for complete integrated workflow with external APIs
    """
    try:
        data = request.get_json() or {}
        
        # Use demo data if none provided
        user_profile = data.get('user_profile', {
            'name': 'Alex Johnson',
            'current_role': 'Senior Software Engineer',
            'skills': ['Python', 'Machine Learning', 'System Design', 'Leadership'],
            'experience_years': 7,
            'industry': 'technology',
            'email': 'alex@example.com',
            'location': 'San Francisco, CA'
        })
        
        career_goals = data.get('career_goals', {
            'target_companies': ['Google', 'Amazon', 'Microsoft'],
            'target_roles': ['Product Manager', 'Engineering Manager'],
            'target_locations': ['San Francisco', 'Remote'],
            'timeline_months': 12,
            'salary_increase_target': 0.25,
            'salary_min': 150000
        })
        
        if USE_REAL_ORCHESTRATOR and hasattr(orchestrator, 'execute_integrated_career_workflow'):
            # Execute the complete integrated workflow
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            try:
                print("🚀 Starting integrated workflow demo...")
                integrated_results = loop.run_until_complete(
                    orchestrator.execute_integrated_career_workflow(
                        user_profile, career_goals
                    )
                )
                
                # Format results for API response
                response = {
                    'status': 'success',
                    'integration_type': 'full_external_apis',
                    'results': {
                        'precision_analysis': integrated_results.precision_analysis,
                        'job_matches': integrated_results.job_matches,
                        'optimized_materials': integrated_results.optimized_materials,
                        'networking_intelligence': integrated_results.networking_intelligence,
                        'application_strategy': integrated_results.application_strategy,
                        'success_predictions': integrated_results.success_predictions,
                        'execution_timeline': integrated_results.execution_timeline,
                        'competitive_insights': integrated_results.competitive_insights
                    },
                    'external_apis_used': [
                        'Jobright.ai (job discovery & networking)',
                        'Jobscan (ATS optimization)', 
                        'Teal (resume generation)',
                        'Precision Career Intelligence (internal AI)'
                    ],
                    'demo_timestamp': datetime.now().isoformat()
                }
                
                loop.close()
                return jsonify(response)
                
            except Exception as e:
                loop.close()
                print(f"❌ Error in integrated workflow: {e}")
                return jsonify({
                    'status': 'error',
                    'integration_type': 'fallback_demo',
                    'error': str(e),
                    'message': 'Integrated workflow failed, check API configurations'
                }), 500
        else:
            return jsonify({
                'status': 'demo_mode',
                'integration_type': 'mock_only',
                'message': 'Real orchestrator not available - using mock implementation',
                'available_features': [
                    'Mock precision analysis',
                    'Mock job discovery',
                    'Mock application strategy'
                ]
            })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e),
            'message': 'Failed to execute integrated demo'
        }), 500

@precision_bp.route('/health', methods=['GET'])
def precision_health_check():
    """Health check for precision career intelligence system"""
    
    # Check orchestrator status
    orchestrator_status = 'real' if USE_REAL_ORCHESTRATOR else 'mock'
    
    features = [
        'Transition path analysis',
        'Transferable skills intelligence', 
        'Company-specific insights',
        'Application strategy optimization',
        'Success prediction modeling'
    ]
    
    if USE_REAL_ORCHESTRATOR:
        features.extend([
            'Jobright.ai job discovery',
            'Jobscan ATS optimization',
            'Teal resume generation',
            'Integrated external API workflow'
        ])
    
    return jsonify({
        'status': 'healthy',
        'system': 'precision_career_intelligence',
        'orchestrator': orchestrator_status,
        'features': features,
        'external_apis_available': USE_REAL_ORCHESTRATOR,
        'timestamp': datetime.now().isoformat()
    })

# Add error handlers
@precision_bp.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found', 'status': 'error'}), 404

@precision_bp.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error', 'status': 'error'}), 500