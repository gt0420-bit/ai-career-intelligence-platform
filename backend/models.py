from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON
import enum

db = SQLAlchemy()

class AgentRole(enum.Enum):
    MARKET_SCOUT = "market_scout"
    OPPORTUNITY_HUNTER = "opportunity_hunter"
    SKILL_STRATEGIST = "skill_strategist"
    CAREER_PLANNER = "career_planner"
    INTELLIGENCE_SYNTHESIZER = "intelligence_synthesizer"

class TaskStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Profile Information
    skills = db.Column(JSON, default=list)
    experience_level = db.Column(db.String(50), default='Mid')
    preferred_locations = db.Column(JSON, default=list)
    target_salary_min = db.Column(db.Integer)
    target_salary_max = db.Column(db.Integer)
    career_goals = db.Column(db.Text)
    
    # Agentic System Settings
    agentic_enabled = db.Column(db.Boolean, default=False)

class Agent(db.Model):
    __tablename__ = 'agents'
    
    id = db.Column(db.String(50), primary_key=True)
    agent_role = db.Column(db.Enum(AgentRole), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class AgentTask(db.Model):
    __tablename__ = 'agent_tasks'
    
    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    agent_id = db.Column(db.String(50), db.ForeignKey('agents.id'), nullable=False)
    
    task_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(TaskStatus), default=TaskStatus.PENDING)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    
    input_context = db.Column(JSON, default=dict)
    output_result = db.Column(JSON, default=dict)

def init_db(app):
    """Initialize the database"""
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        create_default_agents()

def create_default_agents():
    """Create default agents"""
    default_agents = [
        {
            'id': 'market_scout_001',
            'agent_role': AgentRole.MARKET_SCOUT,
            'name': 'Market Intelligence Scout'
        },
        {
            'id': 'opportunity_hunter_001', 
            'agent_role': AgentRole.OPPORTUNITY_HUNTER,
            'name': 'Opportunity Hunter'
        },
        {
            'id': 'intelligence_synthesizer_001',
            'agent_role': AgentRole.INTELLIGENCE_SYNTHESIZER,
            'name': 'Intelligence Synthesizer'
        }
    ]
    
    for agent_data in default_agents:
        existing = Agent.query.get(agent_data['id'])
        if not existing:
            agent = Agent(**agent_data)
            db.session.add(agent)
    
    try:
        db.session.commit()
        print("✅ Default agents created")
    except Exception as e:
        print(f"⚠️  Agent creation error: {e}")
        db.session.rollback()
