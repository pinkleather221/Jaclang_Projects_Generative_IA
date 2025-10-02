# County Water Crisis Reporting & Analysis System

A comprehensive AI-powered water shortage and quality reporting system for Kenyan counties, featuring intelligent analysis with Gemini AI and a real-time web dashboard.

## Project Overview
This system processes water crisis reports from citizens, uses artificial intelligence to classify and analyze issues, and provides actionable insights through both command-line tools and a web-based dashboard. The system successfully analyzed 500 water reports from various areas including Tudor, Mikindani, Changamwe, and others.

## Key Features
- **AI-Powered Analysis** using Gemini 2.0 Flash for intelligent report classification  
- **Real-time Web Dashboard** with interactive data visualizations  
- **Automated Issue Classification** (Shortage, Quality, Infrastructure, Billing, etc.)  
- **Critical Issue Detection** and prioritization  
- **Multi-format Report Generation**  
- **CSV Data Integration** for easy data management  
- **Severity Assessment** (Low, Medium, High, Critical)  

## Technical Architecture
### System Components
- **Data Processing Layer**: CSV file parsing and data validation  
- **AI Analysis Layer**: Gemini AI integration for intelligent classification  
- **Business Logic Layer**: Rule-based fallback classification and trend analysis  
- **Presentation Layer**: Flask web dashboard with Chart.js visualizations  
- **Reporting Layer**: Multiple report formats for different stakeholders  

### Data Flow
1. Load water reports from CSV file  
2. Process each report through AI classification  
3. Aggregate results and identify patterns  
4. Generate visualizations and insights  
5. Serve data through web dashboard and report files  

## Installation Instructions
### Prerequisites
- Python 3.12 or higher  
- Gemini API key from [Google AI Studio](https://aistudio.google.com/)  
- Required Python packages: `google-generativeai`, `flask`  

### Step-by-Step Setup
#### Environment Setup
```bash
# Navigate to project directory
cd Water-Shortage-Reporting-Agent

# Install required packages
pip install google-generativeai flask
```

#### API Configuration
```bash
# Set Gemini API key as environment variable (Windows)
setx GEMINI_API_KEY "your_actual_gemini_api_key_here"

# For immediate use in current session
$env:GEMINI_API_KEY = "your_actual_gemini_api_key_here"
```

#### Data Preparation
- Ensure `water_reports.csv` is in the project directory  
- Required CSV columns: `area`, `report`, `date` (YYYY-MM-DD format)  

## Usage Guide
### Running the System
**Option 1: AI-Powered Analysis**
```bash
python water_agent.py
```
Provides intelligent classification, severity assessment, and recommendations.

**Option 2: Web Dashboard**
```bash
python app.py
```
Access the dashboard at: [http://localhost:5000](http://localhost:5000)

**Option 3: Rule-Based Analysis (No API Required)**
```bash
python working_analyzer.py
```

### Output Files Generated
- `ai_water_crisis_report.txt` – AI analysis with recommendations  
- `smart_water_analysis_report.txt` – Rule-based analysis  
- `county_water_crisis_report.txt` – Executive summary  


## AI Capabilities
The Gemini AI model processes each water report and provides:  
- Issue classification (Shortage, Quality, Infrastructure, Billing, Other)  
- Severity assessment (Low, Medium, High, Critical)  
- Context-aware summaries  
- Specific action recommendations  

**Sample AI Output:**
```
CLASSIFICATION: Quality
SEVERITY: Critical
SUMMARY: Sewage contamination detected in water supply
RECOMMENDATION: Immediate water testing and public health advisory
```

## Dashboard Features
- **Visualizations**: Issue distribution, area-wise analysis, critical issues panel, affected areas list, AI recommendations  
- **Interactive**: Auto-refresh every 30s, responsive design, color-coded severity, priority sorting  

## Analysis Results
From 500 water reports:  
- Quality Issues: 215 (43%)  
- Shortage Issues: 199 (39.8%)  
- Infrastructure Issues: 37 (7.4%)  
- Billing Issues: 25 (5%)  
- Other Issues: 24 (4.8%)  

**Most Affected Areas:** Tudor (58), Mikindani (58), Changamwe (56), Port Reitz (56), Likoni (51)  

**Critical Findings:** 45 severe cases, sewage contamination, extended shortages, infrastructure failures.

## Customization Guide
- Modify classification logic in `water_agent.py` to add new issue types  
- Extend `templates/dashboard.html` for new charts and metrics  
- Add support for databases, APIs, multiple CSVs, Excel  

## API Endpoints
- `GET /` – Dashboard  
- `GET /api/data` – JSON data  
- `GET /api/analyze` – Trigger AI analysis  
- `GET /api/ai-suggestions` – AI-powered recommendations  

## Error Handling
- **API Key Errors**: check `GEMINI_API_KEY`, connectivity, quota  
- **CSV Issues**: correct location, column names, UTF-8 encoding  
- **Dashboard Issues**: check Flask install, port 5000, firewall  

## Performance
- 500+ reports in <2 minutes  
- Real-time dashboard updates  
- Efficient memory usage  
- Works without AI if unavailable  

## Use Cases
- **Government**: monitoring, emergency planning, resource allocation, public health  
- **Service Providers**: operations, maintenance, outage management  
- **Research**: environmental studies, urban planning, crisis management  

## Maintenance and Support
- Update API keys, monitor data quality, update rules, backup reports  
- Troubleshooting: check logs, dependencies, sample data, API docs  

## Future Enhancements
- Mobile app, SMS reporting, predictive analytics, multi-language support, advanced visualization  
- Database integration, authentication, automated scheduling, rate limiting, better error recovery  

## Contributing
Enhancements may include:  
- More visualizations  
- Mapping services integration  
- Advanced ML models  
- Mobile responsive improvements  
- Extra export formats  

## License & Attribution
Developed for educational & governmental use. Comply with Google Gemini API terms and data privacy regulations.

## Support Contact
Provide: issue description, error messages, system environment, sample data.  

**Built for Kenyan County Water Management – Transforming citizen reports into actionable intelligence.**
