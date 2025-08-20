# Report Comparison Tool
A web application that analyzes resident and attending reports and provides a categorized feedback of changes to the resident.

⸻

## 1 Repository structure

```text
Radiologist-Scheduling-Agent/
├─ home.py                          ← Streamlit user interface (entry point)
│
├─ utils/
│   ├─ Ollama_Agent.py
│   ├─ LMStudio_Agent.py
│   └─ OpenAI_Agent.py
│
├─ data/
│   ├─ Example.csv
│   └─ Sample_Reports.csv
│
└─ README.md
```


⸻

## 2 System overview

| **Stage** | **Principal module(s)** | **Summary** |
|-----------|-------------------------|-------------|
| **Data ingestion** | `home.py` | User chooses a model, output format, and single or multi- agent functionality. User then edit prompts to agent(s) and provides resident and attending reports in the provided text boxes. |
| **Agent Call and Analysis** | `utils/Ollama_Agent.py`, `OpenAI_Agent.py` | Agent(s) analyze resident and attending reports and provide an output summarizing the adjustments made to the resident report by the attending. |
| **Presentation layer** | `home.py` | Properly formats the output strings of the agent call and produces wither a sectioned paragraph output or a table output summarizing report adjustments. |

⸻

## 3 Installation and execution

### 3.1 Environment setup

<pre lang="markdown">

<code>
git clone https://github.com/rlacs235711/Report-Comparison-Tool.git
cd Radiologist-Scheduling-Agent

python3 -m venv .venv
source .venv/bin/activate

# Install necessary packages:
pip install -r requirements.txt

# Set your OpenAI API key
export OPENAI_API_KEY=&lt;your-key&gt;
</code>

</pre>

### 3.2 Starting the application
<pre lang="markdown">

<code>
streamlit run ./home.py
</code>

</pre>

The application should open automatically; if not, open the URL shown in the terminal.

⸻

## 4 Operating the application
### 1.	Choose the desired output settings: model, output type, single or multi-agent functionality
### 2.	Edit pre-existing agent prompts (optional)
### 3.	Provide resident and attending reports in the corresponding text boxes
### 4.  Click `Analyze` and wait for output to appear
### 5. Click `📥 Download All Results as CSV` to save all previous inputs and outputs to a csv file

⸻

## 6 Dependencies

The project runs using Python 3.9 + and relies on the following core packages:

| Package         | Purpose                                              |
|----------------|------------------------------------------------------|
| `openai`        | Access to GPT models for parsing tasks              |
| `streamlit`     | Web UI framework                                    |
| `pandas`        | CSV processing                                      |
| `python-dotenv` | Local `.env` management for `OPENAI_API_KEY` (optional) |

Additionally, relevant LLM's downloaded from Ollama are listed below:
### - deepseek-r1:70b
### - llama3.3:latest
### - llama3.2-vision:90b
### - gemma3:27b

New models can be downloaded and utilized by editing the `OLLAMA_MODEL` list in `home.py`.
