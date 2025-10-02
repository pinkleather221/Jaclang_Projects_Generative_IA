from flask import Flask, render_template, jsonify
import os
from water_agent import analyze_with_ai
import json
from datetime import datetime

app = Flask(__name__)

# Sample data for the dashboard
def get_dashboard_data():
    
    return {
        'total_reports': 500,
        'issues_by_type': [
            {'name': 'Quality', 'value': 215, 'color': '#ff6b6b'},
            {'name': 'Shortage', 'value': 199, 'color': '#4ecdc4'},
            {'name': 'Infrastructure', 'value': 37, 'color': '#45b7d1'},
            {'name': 'Billing', 'value': 25, 'color': '#96ceb4'},
            {'name': 'Other', 'value': 24, 'color': '#feca57'}
        ],
        'areas_affected': [
            {'area': 'Tudor', 'reports': 58},
            {'area': 'Mikindani', 'reports': 58},
            {'area': 'Changamwe', 'reports': 56},
            {'area': 'Port Reitz', 'reports': 56},
            {'area': 'Likoni', 'reports': 51},
            {'area': 'Mtwapa', 'reports': 51},
            {'area': 'Nyali', 'reports': 48},
            {'area': 'Kisauni', 'reports': 47},
            {'area': 'Shanzu', 'reports': 38},
            {'area': 'Bamburi', 'reports': 37}
        ],
        'critical_issues': [
            {'area': 'Tudor', 'issue': 'Sewage contamination in water supply', 'severity': 'Critical'},
            {'area': 'Likoni', 'issue': 'No water for 14 consecutive days', 'severity': 'Urgent'},
            {'area': 'Mikindani', 'issue': 'Burst main pipe flooding streets', 'severity': 'Critical'}
        ],
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

@app.route('/')
def dashboard():
    """Main dashboard page"""
    data = get_dashboard_data()
    return render_template('dashboard.html', data=data)

@app.route('/api/analyze')
def api_analyze():
    """API endpoint to run AI analysis"""
    try:
        results = analyze_with_ai()
        return jsonify({
            'success': True,
            'data': results
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })
@app.route('/api/ai-suggestions')
def ai_suggestions():
    """Get AI-powered suggestions"""
    try:
        # This would call the ai analysis
        suggestions = {
            'insights': [
                "Water quality issues are the primary concern affecting 43% of households",
                "Tudor area shows the highest concentration of critical issues",
                "Immediate action needed for sewage contamination cases"
            ],
            'recommendations': [
                "Deploy emergency water purification units to Tudor",
                "Conduct water quality testing in all affected areas",
                "Set up temporary water distribution points in shortage areas"
            ],
            'priority_actions': [
                "Address sewage contamination in Tudor - CRITICAL",
                "Restore water supply to Likoni after 14-day outage - URGENT",
                "Repair burst main pipe in Mikindani - HIGH PRIORITY"
            ]
        }
        return jsonify(suggestions)
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/api/data')
def api_data():
    """API endpoint to get dashboard data"""
    return jsonify(get_dashboard_data())

if __name__ == '__main__':
    # Check if API key is set
    if not os.getenv('GEMINI_API_KEY'):
        print("ERROR: GEMINI_API_KEY environment variable not set!")
        print("Run: setx GEMINI_API_KEY \"your_actual_api_key_here\"")
        exit(1)
    
    print("Starting Flask Web Dashboard...")
    print("Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)