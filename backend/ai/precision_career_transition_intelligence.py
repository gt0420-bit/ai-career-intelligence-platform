#!/usr/bin/env python3
"""
Precision Career Transition Intelligence Layer

Advanced AI system that analyzes transferable skills with unprecedented accuracy
by leveraging historical trends, company-specific patterns, and market intelligence
to help professionals make precision-targeted career transitions.
"""

import asyncio
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import json

class TransitionDifficulty(Enum):
    """Career transition difficulty levels"""
    SEAMLESS = "seamless"           # 90%+ skill overlap
    NATURAL = "natural"             # 70-89% skill overlap  
    STRATEGIC = "strategic"         # 50-69% skill overlap
    AMBITIOUS = "ambitious"         # 30-49% skill overlap
    TRANSFORMATIONAL = "transformational"  # <30% skill overlap

class TransferabilityScore(Enum):
    """How transferable skills are across companies/industries"""
    UNIVERSAL = "universal"         # Transfers everywhere (e.g., leadership)
    INDUSTRY_WIDE = "industry_wide" # Transfers within industry
    COMPANY_SPECIFIC = "company_specific" # Limited to similar companies
    NICHE = "niche"                # Very specific applications

@dataclass
class TransferableSkill:
    """Represents a transferable skill with precision analytics"""
    skill_name: str
    current_proficiency: float  # 0-1 scale
    market_demand: float        # 0-1 scale based on job market data
    transferability_score: TransferabilityScore
    growth_trajectory: float    # Historical growth rate
    companies_valuing: List[str]
    roles_utilizing: List[str]
    skill_evolution_trend: str  # "growing", "stable", "declining"
    certification_boost: Optional[float] = None
    time_to_develop: Optional[int] = None  # months
    
@dataclass
class CareerTransitionPath:
    """Represents a specific career transition pathway"""
    from_role: str
    to_role: str
    target_company: str
    transition_difficulty: TransitionDifficulty
    success_probability: float
    required_skills: List[TransferableSkill]
    skill_gaps: List[str]
    timeline_months: int
    salary_change_percentage: float
    historical_success_examples: List[Dict[str, Any]]
    company_specific_insights: Dict[str, Any]
    precision_strategy: Dict[str, Any]

class PrecisionCareerTransitionIntelligence:
    """
    Advanced AI system for precision career transition analysis
    """
    
    def __init__(self):
        # Import your existing AI systems
        from ai.crewai_career_agents import CrewAICareerSystem
        from ai.vector_career_db import VectorCareerDatabase
        from ai.langchain_career_agent import LangChainCareerAgent
        
        self.crew_ai = CrewAICareerSystem()
        self.vector_db = VectorCareerDatabase()
        self.langchain_agent = LangChainCareerAgent()
        
        # Historical transition data (would be populated from real data)
        self.transition_patterns = self._load_historical_patterns()
        self.company_intelligence = self._load_company_intelligence()
        self.skill_market_data = self._load_skill_market_data()
    
    def _load_historical_patterns(self) -> Dict[str, Any]:
        """Load historical career transition patterns"""
        # Mock data - in production, this would come from your database
        return {
            "software_engineer_to_product_manager": {
                "success_rate": 0.73,
                "avg_timeline_months": 18,
                "key_transferable_skills": ["technical_knowledge", "problem_solving", "user_empathy"],
                "common_skill_gaps": ["stakeholder_management", "market_analysis", "roadmap_planning"],
                "successful_transitions": 847,
                "companies_with_high_success": ["Google", "Microsoft", "Airbnb", "Stripe"]
            },
            "data_scientist_to_ml_engineer": {
                "success_rate": 0.89,
                "avg_timeline_months": 8,
                "key_transferable_skills": ["machine_learning", "python", "statistical_analysis"],
                "common_skill_gaps": ["mlops", "production_systems", "kubernetes"],
                "successful_transitions": 1234,
                "companies_with_high_success": ["Netflix", "Uber", "Tesla", "OpenAI"]
            },
            "consultant_to_strategy_manager": {
                "success_rate": 0.82,
                "avg_timeline_months": 12,
                "key_transferable_skills": ["analytical_thinking", "client_management", "presentation"],
                "common_skill_gaps": ["internal_politics", "long_term_planning", "team_building"],
                "successful_transitions": 623,
                "companies_with_high_success": ["Amazon", "McKinsey", "BCG", "Bain"]
            }
        }
    
    def _load_company_intelligence(self) -> Dict[str, Any]:
        """Load company-specific hiring patterns and preferences"""
        return {
            "Google": {
                "preferred_transition_paths": {
                    "engineer_to_pm": {"success_rate": 0.76, "timeline": 15},
                    "data_scientist_to_research": {"success_rate": 0.84, "timeline": 10}
                },
                "skill_preferences": ["technical_depth", "analytical_rigor", "innovation"],
                "internal_mobility_rate": 0.68,
                "hiring_trends": {
                    "ml_engineers": "high_demand",
                    "product_managers": "competitive", 
                    "researchers": "selective"
                }
            },
            "Amazon": {
                "preferred_transition_paths": {
                    "consultant_to_pm": {"success_rate": 0.71, "timeline": 14},
                    "engineer_to_principal": {"success_rate": 0.63, "timeline": 24}
                },
                "skill_preferences": ["customer_obsession", "ownership", "bias_for_action"],
                "internal_mobility_rate": 0.59,
                "hiring_trends": {
                    "aws_specialists": "very_high_demand",
                    "operations_managers": "steady_demand"
                }
            }
        }
    
    def _load_skill_market_data(self) -> Dict[str, Any]:
        """Load real-time skill market intelligence"""
        return {
            "machine_learning": {
                "market_demand": 0.94,
                "growth_rate": 0.23,
                "avg_salary_premium": 0.35,
                "transferability": TransferabilityScore.INDUSTRY_WIDE,
                "hot_companies": ["OpenAI", "Anthropic", "Google", "Meta"]
            },
            "product_management": {
                "market_demand": 0.87,
                "growth_rate": 0.15,
                "avg_salary_premium": 0.28,
                "transferability": TransferabilityScore.UNIVERSAL,
                "hot_companies": ["Apple", "Google", "Meta", "Stripe"]
            },
            "mlops": {
                "market_demand": 0.91,
                "growth_rate": 0.45,
                "avg_salary_premium": 0.42,
                "transferability": TransferabilityScore.INDUSTRY_WIDE,
                "hot_companies": ["Netflix", "Uber", "Airbnb", "Tesla"]
            }
        }
    
    async def analyze_precision_career_transitions(self, 
                                                 current_profile: Dict[str, Any], 
                                                 target_preferences: Dict[str, Any]) -> List[CareerTransitionPath]:
        """
        Analyze precision career transition opportunities with unprecedented accuracy
        """
        print("🎯 Starting Precision Career Transition Analysis...")
        
        # 1. Analyze current skill profile with market intelligence
        current_skills_analysis = await self._analyze_current_skills(current_profile)
        
        # 2. Identify transferable skills with precision scoring
        transferable_skills = await self._identify_transferable_skills(current_skills_analysis)
        
        # 3. Find strategic transition opportunities
        transition_paths = await self._discover_transition_paths(
            current_profile, transferable_skills, target_preferences
        )
        
        # 4. Apply company-specific intelligence and historical patterns
        enhanced_paths = await self._enhance_with_company_intelligence(transition_paths)
        
        # 5. Create precision targeting strategy for each path
        precision_targeted_paths = await self._create_precision_strategies(enhanced_paths)
        
        return precision_targeted_paths
    
    async def _analyze_current_skills(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze current skills with market intelligence"""
        
        skills_analysis = {}
        current_skills = profile.get('skills', [])
        current_role = profile.get('current_role', '')
        experience_years = profile.get('experience_years', 0)
        
        for skill in current_skills:
            if skill.lower() in self.skill_market_data:
                market_data = self.skill_market_data[skill.lower()]
                
                # Calculate skill strength based on experience and market data
                skill_strength = min(1.0, (experience_years / 10) * 0.7 + 0.3)
                
                skills_analysis[skill] = {
                    'current_strength': skill_strength,
                    'market_demand': market_data['market_demand'],
                    'growth_potential': market_data['growth_rate'],
                    'salary_impact': market_data['avg_salary_premium'],
                    'transferability': market_data['transferability'],
                    'strategic_value': skill_strength * market_data['market_demand']
                }
        
        # Use your CrewAI system for deeper analysis
        crew_analysis = await self.crew_ai.analyze_skill_portfolio(profile)
        
        return {
            'skills_breakdown': skills_analysis,
            'portfolio_strength': np.mean([s['strategic_value'] for s in skills_analysis.values()]),
            'crew_insights': crew_analysis,
            'top_transferable_skills': sorted(skills_analysis.items(), 
                                           key=lambda x: x[1]['strategic_value'], 
                                           reverse=True)[:5]
        }
    
    async def _identify_transferable_skills(self, skills_analysis: Dict[str, Any]) -> List[TransferableSkill]:
        """Identify transferable skills with precision analytics"""
        
        transferable_skills = []
        
        for skill_name, analysis in skills_analysis['skills_breakdown'].items():
            # Create transferable skill object with comprehensive data
            transferable_skill = TransferableSkill(
                skill_name=skill_name,
                current_proficiency=analysis['current_strength'],
                market_demand=analysis['market_demand'],
                transferability_score=analysis['transferability'],
                growth_trajectory=analysis['growth_potential'],
                companies_valuing=self._get_companies_valuing_skill(skill_name),
                roles_utilizing=self._get_roles_utilizing_skill(skill_name),
                skill_evolution_trend="growing" if analysis['growth_potential'] > 0.15 else "stable"
            )
            
            transferable_skills.append(transferable_skill)
        
        return transferable_skills
    
    async def _discover_transition_paths(self, 
                                       current_profile: Dict[str, Any],
                                       transferable_skills: List[TransferableSkill],
                                       preferences: Dict[str, Any]) -> List[CareerTransitionPath]:
        """Discover strategic transition paths using historical data"""
        
        transition_paths = []
        current_role = current_profile.get('current_role', '').lower()
        target_companies = preferences.get('target_companies', [])
        
        # Analyze each potential transition path
        for transition_key, pattern_data in self.transition_patterns.items():
            from_role, to_role = transition_key.split('_to_')
            
            # Check if this transition is relevant
            if from_role in current_role.replace(' ', '_'):
                
                # Calculate transition viability for each target company
                for company in target_companies:
                    if company in self.company_intelligence:
                        company_data = self.company_intelligence[company]
                        
                        # Calculate success probability based on multiple factors
                        base_success_rate = pattern_data['success_rate']
                        company_fit = self._calculate_company_fit(
                            transferable_skills, company_data['skill_preferences']
                        )
                        
                        success_probability = base_success_rate * (0.7 + 0.3 * company_fit)
                        
                        # Determine transition difficulty
                        skill_overlap = self._calculate_skill_overlap(
                            transferable_skills, pattern_data['key_transferable_skills']
                        )
                        
                        difficulty = self._determine_transition_difficulty(skill_overlap)
                        
                        # Create transition path
                        transition_path = CareerTransitionPath(
                            from_role=current_role,
                            to_role=to_role.replace('_', ' ').title(),
                            target_company=company,
                            transition_difficulty=difficulty,
                            success_probability=min(0.95, success_probability),
                            required_skills=self._map_required_skills(pattern_data['key_transferable_skills']),
                            skill_gaps=pattern_data['common_skill_gaps'],
                            timeline_months=pattern_data['avg_timeline_months'],
                            salary_change_percentage=self._estimate_salary_change(current_role, to_role, company),
                            historical_success_examples=self._get_success_examples(transition_key, company),
                            company_specific_insights=company_data,
                            precision_strategy={}  # Will be filled later
                        )
                        
                        transition_paths.append(transition_path)
        
        return sorted(transition_paths, key=lambda x: x.success_probability, reverse=True)
    
    async def _enhance_with_company_intelligence(self, 
                                               transition_paths: List[CareerTransitionPath]) -> List[CareerTransitionPath]:
        """Enhance paths with company-specific intelligence"""
        
        for path in transition_paths:
            company_data = self.company_intelligence.get(path.target_company, {})
            
            # Add company-specific adjustments
            if path.target_company in company_data.get('preferred_transition_paths', {}):
                company_transition_data = company_data['preferred_transition_paths'][f"{path.from_role}_to_{path.to_role}"]
                
                # Adjust success probability based on company preferences
                path.success_probability = min(0.95, 
                    path.success_probability * 1.2 if company_transition_data['success_rate'] > 0.75 else path.success_probability
                )
                
                # Adjust timeline based on company data
                path.timeline_months = int(company_transition_data['timeline'] * 0.9)
            
            # Add hiring trend intelligence
            hiring_trends = company_data.get('hiring_trends', {})
            relevant_trend = None
            
            for role_trend, demand_level in hiring_trends.items():
                if role_trend.lower() in path.to_role.lower():
                    relevant_trend = demand_level
                    break
            
            if relevant_trend:
                path.company_specific_insights['current_hiring_demand'] = relevant_trend
                
                # Boost success probability for high-demand roles
                if relevant_trend in ['high_demand', 'very_high_demand']:
                    path.success_probability = min(0.95, path.success_probability * 1.15)
        
        return transition_paths
    
    async def _create_precision_strategies(self, 
                                         transition_paths: List[CareerTransitionPath]) -> List[CareerTransitionPath]:
        """Create precision-targeted application strategies for each transition path"""
        
        for path in transition_paths:
            # Use your AI agents to create precision strategy
            crew_strategy = await self.crew_ai.create_transition_strategy({
                'transition_path': path,
                'historical_patterns': self.transition_patterns,
                'company_intelligence': path.company_specific_insights
            })
            
            # Create precision targeting strategy
            precision_strategy = {
                'application_timing': self._determine_optimal_timing(path),
                'skill_development_priorities': self._prioritize_skill_development(path),
                'networking_targets': await self._identify_networking_targets(path),
                'portfolio_positioning': self._create_portfolio_strategy(path),
                'interview_preparation': self._create_interview_strategy(path),
                'application_customization': crew_strategy.get('application_strategy', {}),
                'success_accelerators': self._identify_success_accelerators(path)
            }
            
            path.precision_strategy = precision_strategy
        
        return transition_paths
    
    def _determine_optimal_timing(self, path: CareerTransitionPath) -> Dict[str, Any]:
        """Determine optimal timing for transition based on market conditions"""
        company_data = path.company_specific_insights
        
        timing_factors = {
            'current_market_condition': 'favorable',  # Based on hiring trends
            'company_hiring_cycle': self._get_hiring_cycle(path.target_company),
            'skill_gap_closure_time': max(1, len(path.skill_gaps) * 2),  # months
            'optimal_application_window': 'Q1 2025',  # Peak hiring season
            'preparation_timeline': {
                'immediate': 'Update portfolio and LinkedIn',
                '1_month': 'Complete priority skill certifications',
                '3_months': 'Build demonstration projects',
                '6_months': 'Ready for strategic applications'
            }
        }
        
        return timing_factors
    
    def _prioritize_skill_development(self, path: CareerTransitionPath) -> List[Dict[str, Any]]:
        """Prioritize skill development based on impact and feasibility"""
        
        prioritized_skills = []
        
        for skill_gap in path.skill_gaps:
            market_data = self.skill_market_data.get(skill_gap.lower(), {})
            
            priority_score = (
                market_data.get('market_demand', 0.5) * 0.4 +
                market_data.get('growth_rate', 0.1) * 0.3 +
                (1.0 - len(skill_gap.split()) * 0.1) * 0.3  # Simpler skills = higher feasibility
            )
            
            prioritized_skills.append({
                'skill': skill_gap,
                'priority_score': priority_score,
                'development_time': self._estimate_learning_time(skill_gap),
                'learning_resources': self._get_learning_resources(skill_gap),
                'certification_options': self._get_certification_options(skill_gap),
                'impact_on_success': market_data.get('market_demand', 0.5)
            })
        
        return sorted(prioritized_skills, key=lambda x: x['priority_score'], reverse=True)
    
    async def _identify_networking_targets(self, path: CareerTransitionPath) -> List[Dict[str, Any]]:
        """Identify strategic networking targets for the transition"""
        
        # Use vector search to find similar successful transitions
        similar_transitions = self.vector_db.semantic_job_search(
            f"{path.from_role} to {path.to_role} at {path.target_company}",
            n_results=5
        )
        
        networking_targets = [
            {
                'target_type': 'hiring_manager',
                'role': f'{path.to_role} Manager',
                'company': path.target_company,
                'approach': 'Informational interview about role transition',
                'timing': 'Month 2-3 of preparation'
            },
            {
                'target_type': 'recent_transitioner',
                'role': path.to_role,
                'company': path.target_company,
                'approach': 'Connect with someone who made similar transition',
                'timing': 'Month 1 of preparation'
            },
            {
                'target_type': 'internal_advocate',
                'role': 'Current employee in target team',
                'company': path.target_company,
                'approach': 'Build relationship for internal referral',
                'timing': 'Month 3-4 of preparation'
            }
        ]
        
        return networking_targets
    
    # Helper methods (simplified for brevity)
    def _get_companies_valuing_skill(self, skill: str) -> List[str]:
        """Get companies that highly value this skill"""
        return ["Google", "Microsoft", "Amazon", "Meta", "Apple"]  # Mock data
    
    def _get_roles_utilizing_skill(self, skill: str) -> List[str]:
        """Get roles that utilize this skill"""
        return ["Software Engineer", "Data Scientist", "Product Manager"]  # Mock data
    
    def _calculate_company_fit(self, skills: List[TransferableSkill], preferences: List[str]) -> float:
        """Calculate fit between skills and company preferences"""
        return 0.8  # Mock calculation
    
    def _calculate_skill_overlap(self, current_skills: List[TransferableSkill], required_skills: List[str]) -> float:
        """Calculate overlap between current and required skills"""
        return 0.75  # Mock calculation
    
    def _determine_transition_difficulty(self, skill_overlap: float) -> TransitionDifficulty:
        """Determine transition difficulty based on skill overlap"""
        if skill_overlap >= 0.9:
            return TransitionDifficulty.SEAMLESS
        elif skill_overlap >= 0.7:
            return TransitionDifficulty.NATURAL
        elif skill_overlap >= 0.5:
            return TransitionDifficulty.STRATEGIC
        elif skill_overlap >= 0.3:
            return TransitionDifficulty.AMBITIOUS
        else:
            return TransitionDifficulty.TRANSFORMATIONAL
    
    def _map_required_skills(self, skill_names: List[str]) -> List[TransferableSkill]:
        """Map skill names to TransferableSkill objects"""
        return []  # Mock implementation
    
    def _estimate_salary_change(self, from_role: str, to_role: str, company: str) -> float:
        """Estimate salary change percentage"""
        return 0.15  # Mock 15% increase
    
    def _get_success_examples(self, transition_key: str, company: str) -> List[Dict[str, Any]]:
        """Get historical success examples"""
        return [{"name": "Anonymous", "timeline": "14 months", "strategy": "Internal referral"}]
    
    def _get_hiring_cycle(self, company: str) -> str:
        """Get company hiring cycle information"""
        return "Q1 and Q3 peak hiring"
    
    def _estimate_learning_time(self, skill: str) -> str:
        """Estimate time to learn a skill"""
        return "2-4 months"
    
    def _get_learning_resources(self, skill: str) -> List[str]:
        """Get learning resources for a skill"""
        return ["Coursera", "Udemy", "Company training"]
    
    def _get_certification_options(self, skill: str) -> List[str]:
        """Get certification options for a skill"""
        return ["AWS Certification", "Google Cloud", "Industry certification"]
    
    def _create_portfolio_strategy(self, path: CareerTransitionPath) -> Dict[str, Any]:
        """Create portfolio positioning strategy"""
        return {"focus": "Demonstrate transition readiness", "projects": 3}
    
    def _create_interview_strategy(self, path: CareerTransitionPath) -> Dict[str, Any]:
        """Create interview preparation strategy"""
        return {"behavioral": "Focus on adaptability", "technical": "Emphasize transferable skills"}
    
    def _identify_success_accelerators(self, path: CareerTransitionPath) -> List[str]:
        """Identify factors that accelerate transition success"""
        return ["Internal referral", "Relevant certification", "Demonstration project"]

# Example usage
async def demo_precision_career_transition():
    """Demonstrate precision career transition analysis"""
    
    transition_intel = PrecisionCareerTransitionIntelligence()
    
    current_profile = {
        'current_role': 'Senior Software Engineer',
        'skills': ['Python', 'Machine Learning', 'System Design', 'Leadership'],
        'experience_years': 7,
        'industry': 'Technology',
        'company_size': 'Large'
    }
    
    target_preferences = {
        'target_companies': ['Google', 'Amazon', 'Microsoft'],
        'preferred_roles': ['Product Manager', 'Engineering Manager'],
        'timeline': 12,  # months
        'salary_increase_target': 0.25
    }
    
    print("🎯 Analyzing Precision Career Transitions...")
    
    transition_paths = await transition_intel.analyze_precision_career_transitions(
        current_profile, target_preferences
    )
    
    print(f"\n✅ Found {len(transition_paths)} strategic transition paths:")
    
    for i, path in enumerate(transition_paths[:3], 1):  # Show top 3
        print(f"\n{i}. {path.from_role} → {path.to_role} at {path.target_company}")
        print(f"   Success Probability: {path.success_probability:.1%}")
        print(f"   Transition Difficulty: {path.transition_difficulty.value.title()}")
        print(f"   Timeline: {path.timeline_months} months")
        print(f"   Salary Change: {path.salary_change_percentage:+.0%}")
        print(f"   Key Skill Gaps: {', '.join(path.skill_gaps[:3])}")
        
        if path.precision_strategy:
            print(f"   🎯 Precision Strategy:")
            print(f"   • Optimal Timing: {path.precision_strategy['application_timing']['optimal_application_window']}")
            print(f"   • Priority Skills: {len(path.precision_strategy['skill_development_priorities'])} skills identified")
            print(f"   • Networking Targets: {len(path.precision_strategy['networking_targets'])} strategic connections")

if __name__ == "__main__":
    asyncio.run(demo_precision_career_transition())