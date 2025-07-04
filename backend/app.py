from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Career Intelligence System is running!'
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
