from flask import Flask, jsonify, render_template_string
import json

app = Flask(__name__)

# Same HTML as before
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Career Intelligence System</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
    <div class="max-w-4xl mx-auto">
        <h1 class="text-3xl font-bold mb-8 text-center">Career Intelligence System</h1>
        
        <div class="bg-white p-6 rounded-lg shadow-lg mb-6">
            <h2 class="text-xl font-bold mb-4">Skill Strategist</h2>
            
            <div class="space-y-4">
                <input type="text" id="skills" placeholder="Your skills (e.g., Python, JavaScript)" 
                       class="w-full p-3 border rounded" value="Python, JavaScript, SQL">
                <input type="text" id="role" placeholder="Target role (e.g., Senior Developer)" 
                       class="w-full p-3 border rounded" value="Senior Software Engineer">
                <button onclick="analyze()" id="btn" 
                        class="w-full bg-blue-500 text-white p-3 rounded hover:bg-blue-600">
                    Analyze Skills
                </button>
            </div>
        </div>
        
        <div id="results" class="bg-white p-6 rounded-lg shadow-lg hidden">
            <h3 class="text-lg font-bold mb-4">Results</h3>
            <div id="output" class="bg-gray-50 p-4 rounded max-h-96 overflow-auto"></div>
        </div>
    </div>

    <script>
        async function analyze() {
            const btn = document.getElementById('btn');
            const results = document.getElementById('results');
            const output = document.getElementById('output');
            
            btn.textContent = 'Analyzing...';
            btn.disabled = true;
            
            try {
                const response = await fetch('/analyze', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        skills: document.getElementById('skills').value,
                        role: document.getElementById('role').value
                    })
                });
                
                const data = await response.json();
                
                // Better formatting
                output.innerHTML = '<pre style="white-space: pre-wrap; font-family: monospace;">' + 
                                 JSON.stringify(data, null, 2) + '</pre>';
                results.classList.remove('hidden');
                
                // Scroll to results
                results.scrollIntoView({ behavior: 'smooth' });
                
            } catch (error) {
                output.innerHTML = '<p class="text-red-500">Error: ' + error.message + '</p>';
                results.classList.remove('hidden');
            }
            
            btn.textContent = 'Analyze Skills';
            btn.disabled = false;
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/analyze', methods=['POST'])
def analyze():
    print("🔍 Starting comprehensive agent analysis...")
    
    try:
        # Import the agent
        from agents.skill_strategist_agent import SkillStrategistAgent
        agent = SkillStrategistAgent()
        print(f"✅ Agent created: {type(agent)}")
        
        # Call the agent
        print("🚀 Calling execute_task...")
        result = agent.execute_task('skill_gap_analysis')
        print(f"📊 Raw result type: {type(result)}")
        print(f"📊 Raw result content: {result}")
        
        # Inspect the result object thoroughly
        result_info = {
            'raw_result': str(result),
            'result_type': str(type(result)),
            'result_length': len(str(result)) if result else 0
        }
        
        # If result has attributes, get them all
        if hasattr(result, '__dict__'):
            result_info['attributes'] = {}
            for key, value in result.__dict__.items():
                try:
                    # Try to make it JSON serializable
                    json.dumps(value)
                    result_info['attributes'][key] = value
                except:
                    result_info['attributes'][key] = str(value)
            print(f"📋 Result attributes: {result_info['attributes']}")
        
        # If result is a dict
        if isinstance(result, dict):
            result_info['dict_content'] = result
            print(f"📋 Result dict: {result}")
        
        # Check if agent has other useful methods
        agent_methods = [method for method in dir(agent) if not method.startswith('_')]
        result_info['agent_methods'] = agent_methods
        print(f"🔧 Agent methods: {agent_methods}")
        
        # Try to get more detailed output
        detailed_result = {
            'status': 'success',
            'agent_analysis': result_info,
            'timestamp': str(__import__('datetime').datetime.now())
        }
        
        print(f"✅ Sending response: {detailed_result}")
        return jsonify(detailed_result)
        
    except Exception as e:
        import traceback
        error_info = {
            'status': 'error',
            'error': str(e),
            'traceback': traceback.format_exc(),
            'timestamp': str(__import__('datetime').datetime.now())
        }
        print(f"❌ Error occurred: {error_info}")
        return jsonify(error_info)

if __name__ == '__main__':
    print("🧪 Starting ENHANCED Career Intelligence System")
    print("🌐 Go to: http://localhost:5003")
    app.run(debug=True, port=5003)
