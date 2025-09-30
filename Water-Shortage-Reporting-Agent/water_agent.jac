import random;
import from byllm.llm {Model}

#configure the llm , using the GGEMINI_API_KEY environment variable
glob llm =Model(model_name - "gemini/gemini-2.5-flash", verbose=False);

#Acontract for te llm to perfom classification and summarization 
def analyze_report(report_text: str) -> str

 """
    Analyze the user report text. 
    1. Classify the issue as 'Shortage', 'Quality', or 'Infrastructure'.
    2. Provide a brief (one sentence) summary suitable for a county dashboard.
    
    Format the output as: Classification: [TYPE] | Summary: [SUMMARY]
    """ 
    by llm();
    walker ReportProcessor{
        has report_data: list[str];
        has classified_reports: list[str] = [];
        can analyze_report;

        #The entry point of the walker
        can start with `root entry {
            print("Starting water report analysis...");
            #Simulated user-submitted reports for various areas 
            
        }
    }