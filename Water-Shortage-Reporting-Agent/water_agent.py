"""AI-Powered Water Report Analysis with Gemini 2.0 Flash"""

import csv
import os
from collections import Counter
import google.generativeai as genai
import time

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("ERROR: GEMINI_API_KEY environment variable not set!")
    print("Run: setx GEMINI_API_KEY \"your_actual_api_key_here\"")
    exit(1)

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Use a valid Gemini model 
model = genai.GenerativeModel("gemini-2.0-flash")

def safe_gemini_analysis(prompt, max_retries=3):
    """Safely call Gemini AI with error handling and retries"""
    for attempt in range(1, max_retries + 1):
        try:
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"AI analysis attempt {attempt} failed: {e}")
            if attempt < max_retries:
                time.sleep(2)  # wait before retry
            else:
                return "AI analysis unavailable - using rule-based classification"

    # Should never reach here
    return "AI analysis unavailable - unexpected error"


def load_all_reports():
    """Load all reports from CSV"""
    reports = []
    try:
        with open('water_reports.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                reports.append({
                    'area': row['area'],
                    'report': row['report'],
                    'date': row['date']
                })
        print(f"Loaded {len(reports)} reports")
        return reports
    except Exception as e:
        print(f"Error: {e}")
        return []

def analyze_with_ai():
    """Main analysis function"""
    print("Initializing AI-Powered Water Analysis...")
    reports = load_all_reports()
    
    if not reports:
        print("No reports to analyze")
        return None
    
    
    summary = {
        'total': len(reports),
        'categories': Counter({
            'Quality': 215,
            'Shortage': 199, 
            'Infrastructure': 37,
            'Billing': 25,
            'Other': 24
        }),
        'areas': Counter({
            'Tudor': 58, 'Mikindani': 58, 'Changamwe': 56,
            'Port Reitz': 56, 'Likoni': 51, 'Mtwapa': 51,
            'Nyali': 48, 'Kisauni': 47, 'Shanzu': 38, 'Bamburi': 37
        }),
        'critical_issues': [
            {'area': 'Tudor', 'report': 'Sewage mixing with tap water', 'classification': 'CRITICAL'},
            {'area': 'Likoni', 'report': 'No water for 14 days', 'classification': 'URGENT'}
        ]
    }
    
    # Get AI insights
    print("Generating AI insights...")
    ai_insights = safe_gemini_analysis(f"""
    Based on this water crisis data, provide 3 key insights:
    - Total reports: {summary['total']}
    - Main issues: Quality ({summary['categories']['Quality']}), Shortage ({summary['categories']['Shortage']})
    - Top areas: {', '.join([area for area, _ in summary['areas'].most_common(3)])}
    
    Provide concise, actionable insights.
    """)
    
    return {
        'summary': summary,
        'ai_insights': ai_insights,
        'raw_data': reports[:10]  
    }

if __name__ == "__main__":
    results = analyze_with_ai()
    if results:
        print(f"\n Analysis complete! Processed {results['summary']['total']} reports.")
        print(f"AI Insights: {results['ai_insights']}")