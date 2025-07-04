from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple HTML template embedded in Python
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Career Intelligence Test</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
        .result { margin-top: 20px; padding: 20px; background: #f8f9fa; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Career Intelligence System - Test</h1>
    
    <h2>Test Endpoints</h2>
    
    <button onclick="testHealth()">Test Health Check</button>
    <button onclick="testSkillAnalysis()">Test Skill Analysis</button>
    
    <div id="result" class="result" style="display:none;"></div>

    <script>
        function showResult(data) {
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
        }

        async function testHealth() {
            try {
                const response = await fetch('/api/health');
                const data = await response.json();
                showResult({status: 'Health Check', data: data});
            } catch (error) {
                showResult({status: 'Health Check Error', error: error.message});
            }
        }

        async function testSkillAnalysis() {
            try {
                console.log('Making POST request to /api/skill-analysis');
                const response = await fetch('/api/skill-analysis', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        currentSkills: 'Python, JavaScript',
                        targetRole: 'Senior Developer'
                    })
                });
                
                console.log('Response received:', response.status, response.statusText);
                
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }
                
                const data = await response.json();
                showResult({status: 'Skill Analysis Success', data: data});
            } catch (error) {
                console.error('Error:', error);
                showResult({status: 'Skill Analysis Error', error: error.message});
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'Test server running!'})

@app.route('/api/skill-analysis', methods=['POST'])
def skill_analysis():
    try:
        data = request.get_json()
        print(f"✅ Received POST request: {data}")
        
        # Return a simple test response
        result = {
            'success': True,
            'message': 'Skill analysis working!',
            'received_data': data,
            'confidence': 95,
            'execution_time': 2.5
        }
        
        print(f"✅ Sending response: {result}")
        return jsonify(result)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    print("🧪 Starting TEST server...")
    print("🌐 Go to: http://localhost:5002")
    app.run(debug=True, host='0.0.0.0', port=5002)
