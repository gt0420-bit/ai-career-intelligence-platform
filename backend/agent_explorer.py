from flask import Flask, jsonify, render_template_string
import json

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Agent Explorer</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
    <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl font-bold mb-8 text-center">Career Intelligence Agent Explorer</h1>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
            <button onclick="testMethod('execute_task')" class="bg-blue-500 text-white p-4 rounded hover:bg-blue-600">
                Test execute_task
            </button>
            <button onclick="testMethod('stats')" class="bg-green-500 text-white p-4 rounded hover:bg-green-600">
                Check stats
            </button>
            <button onclick="testMethod('config')" class="bg-purple-500 text-white p-4 rounded hover:bg-purple-600">
                View config
            </button>
            <button onclick="testMethod('skill_market_data')" class="bg-orange-500 text-white p-4 rounded hover:bg-orange-600">
                Get skill_market_data
            </button>
            <button onclick="testMethod('learning_time_estimates')" class="bg-pink-500 text-white p-4 rounded hover:bg-pink-600">
                Get learning_time_estimates
            </button>
            <button onclick="testMethod('generate_autonomous_tasks')" class="bg-indigo-500 text-white p-4 rounded hover:bg-indigo-600">
                Generate autonomous tasks
            </button>
        </div>
        
        <div id="results" class="bg-white p-6 rounded-lg shadow-lg">
            <h3 class="text-lg font-bold mb-4">Results</h3>
            <div id="output" class="bg-gray-50 p-4 rounded max-h-96 overflow-auto">
                Click a button to explore your agent's capabilities!
            </div>
        </div>
    </div>

    <script>
        async function testMethod(method) {
            const output = document.getElementById('output');
            output.innerHTML = '<p class="text-blue-500">Testing ' + method + '...</p>';
            
            try {
                const response = await fetch('/test/' + method, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({})
                });
                
                const data = await response.json();
                output.innerHTML = '<h4 class="font-bold mb-2">Method: ' + method + '</h4><pre style="white-space: pre-wrap; font-family: monospace;">' + 
                                 JSON.stringify(data, null, 2) + '</pre>';
                
            } catch (error) {
                output.innerHTML = '<p class="text-red-500">Error testing ' + method + ': ' + error.message + '</p>';
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/test/<method>', methods=['POST'])
def test_method(method):
    print(f"🔍 Testing method: {method}")
    
    try:
        from agents.skill_strategist_agent import SkillStrategistAgent
        agent = SkillStrategistAgent()
        
        result_info = {
            'method': method,
            'status': 'success',
            'timestamp': str(__import__('datetime').datetime.now())
        }
        
        if method == 'execute_task':
            print("🚀 Calling execute_task...")
            result = agent.execute_task('skill_gap_analysis')
            print(f"Raw result: {result}")
            print(f"Result type: {type(result)}")
            
            # Try to get all attributes of the result
            if hasattr(result, '__dict__'):
                result_info['result_attributes'] = {}
                for key, value in result.__dict__.items():
                    try:
                        json.dumps(value)
                        result_info['result_attributes'][key] = value
                    except:
                        result_info['result_attributes'][key] = str(value)
            
            # Try common AgentResult attributes
            common_attrs = ['success', 'result', 'error', 'data', 'output', 'response', 'content', 'message']
            result_info['common_attributes'] = {}
            for attr in common_attrs:
                if hasattr(result, attr):
                    try:
                        val = getattr(result, attr)
                        json.dumps(val)
                        result_info['common_attributes'][attr] = val
                    except:
                        result_info['common_attributes'][attr] = str(val)
            
            result_info['raw_result'] = str(result)
            
        elif method == 'stats':
            result_info['stats'] = getattr(agent, 'stats', 'No stats available')
            
        elif method == 'config':
            config = getattr(agent, 'config', {})
            result_info['config'] = str(config) if not isinstance(config, dict) else config
            
        elif method == 'skill_market_data':
            try:
                market_data = agent.skill_market_data
                result_info['skill_market_data'] = str(market_data) if not isinstance(market_data, dict) else market_data
            except Exception as e:
                result_info['skill_market_data'] = f"Error accessing: {str(e)}"
                
        elif method == 'learning_time_estimates':
            try:
                estimates = agent.learning_time_estimates
                result_info['learning_time_estimates'] = str(estimates) if not isinstance(estimates, dict) else estimates
            except Exception as e:
                result_info['learning_time_estimates'] = f"Error accessing: {str(e)}"
                
        elif method == 'generate_autonomous_tasks':
            try:
                tasks = agent.generate_autonomous_tasks()
                result_info['autonomous_tasks'] = str(tasks)
            except Exception as e:
                result_info['autonomous_tasks'] = f"Error calling: {str(e)}"
        
        print(f"✅ Method {method} result: {result_info}")
        return jsonify(result_info)
        
    except Exception as e:
        import traceback
        error_info = {
            'method': method,
            'status': 'error',
            'error': str(e),
            'traceback': traceback.format_exc()
        }
        print(f"❌ Error testing {method}: {error_info}")
        return jsonify(error_info)

if __name__ == '__main__':
    print("🔍 Starting Agent Explorer")
    print("🌐 Go to: http://localhost:5004")
    app.run(debug=True, port=5004)
