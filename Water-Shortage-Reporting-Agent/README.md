 # Jaclang Projects for Kenyan Challenges

This repository contains two simple yet innovative projects built using **Jaclang**, focusing on solving common problems in Kenyan urban centers like Mombasa and Nairobi.


| **1. Water Shortage Reporting Agent** | Classifying user reports on water issues (quality, shortage, infrastructure). | LLM-backed Reasoning (`byllm` extension) |
| **2. Traffic Fine Data Cleaner** | Cleaning and aggregating inconsistent traffic fine records. | Built-in Graph and Data Manipulation |

## 🛠️ Prerequisites

To run both projects, you need to have **Python 3.10+** and **Jaclang** installed, along with the required extensions.

1.  **Set up your environment (if you haven't already):**
    ```bash
    python -m venv jac-env
    .\jac-env\Scripts\activate  # On Windows PowerShell
    # source jac-env/bin/activate  # On Linux/macOS
    ```

2.  **Install Jaclang and the LLM extension:**
    ```bash
    pip install jaclang byllm
    ```

3.  **Set your Gemini API Key:** The Water Agent requires a valid Gemini API key for the LLM call. Set it as an environment variable:
    ```powershell
    # On Windows PowerShell:
    $env:GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY"

    # On Linux/macOS:
    # export GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY"
    ```

***

## 1. Water Shortage Reporting Agent

This project simulates a system where public reports on water issues are automatically classified and summarized using the Gemini LLM.

### 📁 Project Files

| File | Description |
| :--- | :--- |
| `water_agent.jac` | The main Jac code defining the `ReportProcessor` walker, the LLM-backed function (`analyze_report`), and the core workflow. |
| `water_agent.impl.jac` | The implementation file, which holds the prompt (docstring) for the LLM to guide its classification task. |

### 🚀 How to Run

1.  Ensure your `GEMINI_API_KEY` is set (see Prerequisites).
2.  Run the main Jac file:

    ```bash
    jac run water_agent.jac
    ```

### Expected Output

The program will process the simulated reports, calling the LLM for each one, and provide a final aggregated summary: