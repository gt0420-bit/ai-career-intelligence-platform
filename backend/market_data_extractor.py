from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Market Data Extractor</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
    <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl font-bold mb-8 text-center">Market Scout Real Data Extractor</h1>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <button onclick="getJobSources()" class="bg-blue-500 text-white p-4 rounded hover:bg-blue-600">
                Get job_sources
            </button>
            <button onclick="getMonitoredCompanies()" class="bg-green-500 text-white p-4 rounded hover:bg-green-600">
                Get monitored_companies
            </button>
            <button onclick="getHeaders()" class="bg-purple-500 text-white p-4 rounded hover:bg-purple-600">
                Get headers
            </button>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
            <button onclick="testAllMethods()" class="bg-orange-500 text-white p-4 rounded hover:bg-orange-600">
                Test All Methods
            </button>
            <button onclick="getCompleteData()" class="bg-red-500 text-white p-4 rounded hover:bg-red-600">
                Get Complete Market Data
            </button>
        </div>
        
        <div id="results" class="bg-white p-6 rounded-lg shadow-lg">
            <h3 class="text-lg font-bold mb-4">Real Market Data</h3>
            <div id="output" class="bg-gray-50 p-4 rounded max-h-96 overflow-auto">
                Click buttons to extract real market data from your agent!
            </div>
        </div>
    </div>

    <script>
        async function getJobSources() {
            await fetchData('/get-job-sources', 'Getting job sources...');
        }

        async function getMonitoredCompanies() {
            await fetchData('/get-monitored-companies', 'Getting monitored companies...');
        }

        async function getHeaders() {
            await fetchData('/get-headers', 'Getting headers...');
        }

        async function testAllMethods() {
            await fetchData('/test-all-methods', 'Testing all methods...');
        }

        async function getCompleteData() {
            await fetchData('/get-complete-data', 'Getting complete market data...');
        }

        async function fetchData(endpoint, loadingMsg) {
            const output = document.getElementById('output');
            output.innerHTML = '<p class="text-blue-500">' + loadingMsg + '</p>';
            
            try {
                const response = await fetch(endpoint, { method: 'POST' });
                const data = await response.json();
                output.innerHTML = '<pre style="white-space: pre-wrap; font-family: monospace; font-size: 12px;">' + 
                                 JSON.stringify(data, null, 2) + '</pre>';
            } catch (error) {
                output.innerHTML = '<p class="text-red-500">Error: ' + error.message + '</p>';
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/get-job-sources', methods=['POST'])
def get_job_sources():
    try:
        from agents.market_scout_agent import MarketScoutAgent
        agent = MarketScoutAgent()
        
        job_sources = getattr(agent, 'job_sources', None)
        
        return jsonify({
            'property': 'job_sources',
            'type': str(type(job_sources)),
            'data': job_sources,
            'length': len(job_sources) if hasattr(job_sources, '__len__') else 0
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get-monitored-companies', methods=['POST'])
def get_monitored_companies():
    try:
        from agents.market_scout_agent import MarketScoutAgent
        agent = MarketScoutAgent()
        
        companies = getattr(agent, 'monitored_companies', None)
        
        return jsonify({
            'property': 'monitored_companies',
            'type': str(type(companies)),
            'data': companies,
            'length': len(companies) if hasattr(companies, '__len__') else 0
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get-headers', methods=['POST'])
def get_headers():
    try:
        from agents.market_scout_agent import MarketScoutAgent
        agent = MarketScoutAgent()
        
        headers = getattr(agent, 'headers', None)
        
        return jsonify({
            'property': 'headers',
            'type': str(type(headers)),
            'data': headers
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/test-all-methods', methods=['POST'])
def test_all_methods():
    try:
        from agents.market_scout_agent import MarketScoutAgent
        agent = MarketScoutAgent()
        
        results = {}
        
        # Test each method we found
        methods = ['agent_id', 'agent_role', 'is_active']
        
        for method_name in methods:
            try:
                if hasattr(agent, method_name):
                    attr = getattr(agent, method_name)
                    if callable(attr):
                        try:
                            result = attr()
                            results[method_name] = {
                                'callable': True,
                                'result': result,
                                'type': str(type(result))
                            }
                        except Exception as e:
                            results[method_name] = {
                                'callable': True,
                                'error': str(e)
                            }
                    else:
                        results[method_name] = {
                            'callable': False,
                            'value': attr,
                            'type': str(type(attr))
                        }
            except Exception as e:
                results[method_name] = {'error': str(e)}
        
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get-complete-data', methods=['POST'])
def get_complete_data():
    try:
        from agents.market_scout_agent import MarketScoutAgent
        agent = MarketScoutAgent()
        
        # Get all the data we can find
        complete_data = {
            'agent_info': {
                'type': str(type(agent)),
                'agent_id': getattr(agent, 'agent_id', None),
                'agent_role': getattr(agent, 'agent_role', None)
            },
            'market_data': {
                'job_sources': getattr(agent, 'job_sources', None),
                'monitored_companies': getattr(agent, 'monitored_companies', None),
                'headers': getattr(agent, 'headers', None)
            },
            'stats': getattr(agent, 'stats', None),
            'config': getattr(agent, 'config', None)
        }
        
        # Execute the task to see if we get different data
        try:
            task_result = agent.execute_task('daily_market_scan')
            complete_data['task_execution'] = {
                'result': str(task_result),
                'type': str(type(task_result))
            }
            
            # If it's an object with attributes, extract them
            if hasattr(task_result, '__dict__'):
                complete_data['task_execution']['attributes'] = {}
                for key, value in task_result.__dict__.items():
                    try:
                        import json
                        json.dumps(value)
                        complete_data['task_execution']['attributes'][key] = value
                    except:
                        complete_data['task_execution']['attributes'][key] = str(value)
        except Exception as e:
            complete_data['task_execution'] = {'error': str(e)}
        
        return jsonify(complete_data)
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': __import__('traceback').format_exc()})

if __name__ == '__main__':
    print("🔍 Starting Market Data Extractor")
    print("🌐 Go to: http://localhost:5006")
    app.run(debug=True, port=5006)
