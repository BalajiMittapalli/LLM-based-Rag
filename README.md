# Retrieval-Augmented Generation (RAG) System with LLM Integration

This project implements a Retrieval-Augmented Generation (RAG) system powered by a Large Language Model (LLM). The system seamlessly integrates a front-end interface with a backend service to scrape, process, and generate responses to user queries. The architecture comprises the following components:

- **Streamlit Frontend**: Delivers an intuitive user interface for interaction.
- **Flask Backend**: Manages API requests, content scraping, and LLM integration.
- **Large Language Model (LLM)**: Generates contextually relevant responses from processed data.

## Key Features  
- **User Interaction**: Users can submit queries via the Streamlit-based interface.  
- **Content Retrieval**: The system retrieves relevant articles from the web based on user queries.  
- **Content Processing**: Scraped content is refined for LLM consumption.  
- **Response Generation**: The LLM generates accurate and insightful responses from the processed content.  
- **Conversational Memory (Bonus)**: Optional integration with tools like LangChain to maintain conversational context.

## Prerequisites  
- Python 3.8 or higher  
- API Keys: Required for web scraping and LLM integration (to be provided in the `.env` file)

## Setup Instructions  

### Step 1: Clone the Repository  
Clone the repository and navigate into the project folder:  
```bash
git clone https://github.com/BalajiMittapalli/LLM-based-Rag.git

Step 2: Set Up a Virtual Environment
You can use venv or conda to create an isolated environment for this project.
Using venv
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

Using conda
conda create --name project_env python=3.8
conda activate project_env

Step 3: Install Dependencies
Install the required packages listed in requirements.txt.
pip install -r requirements.txt

Step 4: Configure Environment Variables
Create a .env file in the root directory and add your API keys:
# Example .env file
GEMINI_API_KEY=your_gemini_api_key

Step 5: Run the Flask Backend
Navigate to the flask_app directory and start the Flask server:
cd flask_app
python app.py

Step 6: Run the Streamlit Frontend
In a new terminal, navigate to the streamlit_app directory and run the Streamlit app:
cd streamlit_app
streamlit run app.py

Step 7: Open the Application
Open your web browser and go to http://localhost:8501. You can now interact with the system by entering your queries.

