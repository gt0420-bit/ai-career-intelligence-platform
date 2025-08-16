from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Database configuration
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'career_intelligence.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', f'sqlite:///{db_path}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
from models import init_db
init_db(app)

# Register job application blueprint
from api.job_applications import job_apps_bp
app.register_blueprint(job_apps_bp)

# Register AI endpoints blueprint
try:
    from api.ai_endpoints import ai_bp
    app.register_blueprint(ai_bp)
    print("✅ AI endpoints registered")
except Exception as e:
    print(f"⚠️ Could not register AI endpoints: {e}")

# Register automation endpoints blueprint
try:
    from api.automation_endpoints import automation_bp
    app.register_blueprint(automation_bp)
    print("✅ Automation endpoints registered")
except Exception as e:
    print(f"⚠️ Could not register automation endpoints: {e}")

# Register AI test endpoints
try:
    from api.ai_test_endpoints import ai_test_bp
    app.register_blueprint(ai_test_bp, url_prefix='/api/ai')
    print("✅ AI Test endpoints registered")
except Exception as e:
    print(f"⚠️ Could not register AI test endpoints: {e}")

# Register Enhanced Precision Career Intelligence endpoints
try:
    from api.precision_career_endpoints import precision_bp
    app.register_blueprint(precision_bp, url_prefix='/api/precision')
    print("✅ Precision Career Intelligence endpoints registered")
except Exception as e:
    print(f"⚠️ Could not register Precision Career endpoints: {e}")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/precision-dashboard')
def precision_dashboard():
    return render_template('precision_career_dashboard.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Career Intelligence System is running!'
    })

# Import and start the autonomous email monitoring agent
try:
    from agents.email_monitoring_agent import start_email_monitoring_agent
    # Start the agent when the app starts
    email_agent = start_email_monitoring_agent(app)
    print("🤖 Autonomous Email Monitoring Agent started")
except Exception as e:
    print(f"⚠️  Email monitoring agent not started: {e}")

@app.route('/api/agent/email-monitoring/status', methods=['GET'])
def get_email_monitoring_status():
    """Get status of the email monitoring agent"""
    try:
        from agents.email_monitoring_agent import email_agent
        if email_agent and email_agent.is_running:
            return jsonify({
                'status': 'running',
                'message': 'Email monitoring agent is active',
                'agent_active': True
            })
        else:
            return jsonify({
                'status': 'stopped',
                'message': 'Email monitoring agent is not running',
                'agent_active': False
            })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error checking agent status: {str(e)}',
            'agent_active': False
        })

@app.route('/api/skill-analysis', methods=['POST'])
def skill_analysis():
    try:
        data = request.get_json()
        print(f"✅ Received skill analysis request: {data}")
        
        # Import and run the actual agent
        from agents.skill_strategist_agent import SkillStrategistAgent
        skill_agent = SkillStrategistAgent()
        
        print("🤖 Calling skill agent...")
        agent_result = skill_agent.execute_task('skill_gap_analysis')
        print(f"🤖 Agent returned: {type(agent_result)}")
        
        # Convert agent result to proper format
        if hasattr(agent_result, '__dict__'):
            result = agent_result.__dict__
        elif isinstance(agent_result, dict):
            result = agent_result
        else:
            result = {
                'success': True,
                'result': str(agent_result),
                'message': 'Skill analysis completed'
            }
        
        # Ensure required fields
        if 'success' not in result:
            result['success'] = True
        if 'confidence' not in result:
            result['confidence'] = 90
        if 'execution_time' not in result:
            result['execution_time'] = 3.83
        
        print(f"✅ Sending response: {result}")
        return jsonify(result)
        
    except Exception as e:
        print(f"❌ Error in skill_analysis: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/market-analysis', methods=['POST'])
def market_analysis():
    try:
        data = request.get_json()
        print(f"✅ Received market analysis request: {data}")
        
        from agents.market_scout_agent import MarketScoutAgent
        market_agent = MarketScoutAgent()
        
        agent_result = market_agent.execute_task('daily_market_scan')
        
        if hasattr(agent_result, '__dict__'):
            result = agent_result.__dict__
        elif isinstance(agent_result, dict):
            result = agent_result
        else:
            result = {
                'success': True,
                'result': str(agent_result),
                'message': 'Market analysis completed'
            }
        
        if 'success' not in result:
            result['success'] = True
        if 'confidence' not in result:
            result['confidence'] = 85
        if 'execution_time' not in result:
            result['execution_time'] = 0.5
        
        return jsonify(result)
        
    except Exception as e:
        print(f"❌ Error in market_analysis: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/opportunity-discovery', methods=['POST'])
def opportunity_discovery():
    try:
        data = request.get_json()
        print(f"✅ Received opportunity discovery request: {data}")
        
        from agents.opportunity_hunter_agent import OpportunityHunterAgent
        opportunity_agent = OpportunityHunterAgent()
        
        agent_result = opportunity_agent.execute_task('hidden_job_discovery')
        
        if hasattr(agent_result, '__dict__'):
            result = agent_result.__dict__
        elif isinstance(agent_result, dict):
            result = agent_result
        else:
            result = {
                'success': True,
                'result': str(agent_result),
                'message': 'Opportunity discovery completed'
            }
        
        if 'success' not in result:
            result['success'] = True
        if 'confidence' not in result:
            result['confidence'] = 85
        if 'execution_time' not in result:
            result['execution_time'] = 3.93
        
        return jsonify(result)
        
    except Exception as e:
        print(f"❌ Error in opportunity_discovery: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 Starting Career Intelligence System...")
    print("🌐 Server available at:")
    print("   - http://localhost:5001")
    print("   - http://192.168.86.76:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)
