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
Clone the Repository: Start by cloning the repository from GitHub using the following command:  
```bash
git clone https://github.com/BalajiMittapalli/LLM-based-Rag.git

Step 2: Create a Virtual Environment
You can use either venv or conda to create an isolated environment for this project.
Using venv
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

Using conda
conda create --name project_env python=3.8
conda activate project_env

Step 3: Install Required Packages
Install the necessary dependencies listed in the requirements.txt file by running
pip install -r requirements.txt

Step 4: Set Up Environment Variables
Create a .env file in the root folder and add your API keys.
For example:
GEMINI_API_KEY=your_gemini_api_key

Step 5: Launch the Flask Backend
Navigate to the flask_app directory and start the Flask server by executing:
cd flask_app
python app.py

Step 6: Run the Streamlit Frontend
Open a new terminal, go to the streamlit_app directory, and run the Streamlit app:
cd streamlit_app
streamlit run app.py

Step 7: Access the Application
Open your browser and visit http://localhost:8501 to interact with the system by entering your queries.

