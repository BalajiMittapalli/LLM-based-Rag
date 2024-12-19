from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Load the Gemini API key
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Check if the API key is loaded
if not GEMINI_API_KEY:
    raise ValueError("API key for Gemini is not set in the environment variables.")

# Set the API endpoint for Gemini
API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

app = Flask(__name__)

# Function to search articles
def search_articles(query):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [{"parts": [{"text": query}]}]
    }

    # Log the request being sent
    print(f"Sending request to Gemini API with data: {data}")
    
    try:
        response = requests.post(f"{API_ENDPOINT}?key={GEMINI_API_KEY}", json=data, headers=headers)
        
        print(f"Raw API response: {response.status_code} {response.text}")
        
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching articles: {str(e)}")

    results = response.json()
    
    print(f"Parsed API response: {results}")

    articles = []

    for item in results.get('candidates', []):
        article_content = item.get('content', {}).get('parts', [{}])[0].get('text', '')
        articles.append({"content": article_content})

    return articles

# Route to handle queries from the frontend
@app.route('/query', methods=['POST'])
def handle_query():
    try:
        # Get the query from the request
        data = request.get_json()
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "No query provided"}), 400

        # Log the received query
        print(f"Received query: {query}")

        # Step 1: Search for relevant articles based on the query
        try:
            articles = search_articles(query)
        except Exception as e:
            return jsonify({"error": f"Error searching articles: {str(e)}"}), 500

        # Step 2: Concatenate the article contents
        content = concatenate_content(articles)

        # Step 3: Generate the answer based on the content and query
        answer = generate_answer(content, query)

        # Return the response as JSON
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function to concatenate article contents
def concatenate_content(articles):
    full_text = ' '.join(article.get('content', '') for article in articles)
    return full_text

# Function to generate an answer based on the content
def generate_answer(content, query):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [{"parts": [{"text": f"Based on the following content, answer the query: {query}\n\nContent: {content}"}]}]
    }

    try:
        response = requests.post(f"{API_ENDPOINT}?key={GEMINI_API_KEY}", json=data, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error generating answer: {str(e)}")

    results = response.json()

    # Extract the answer from the response
    if 'candidates' in results and len(results['candidates']) > 0:
        return results['candidates'][0].get('content', {}).get('parts', [{}])[0].get('text', '').strip()
    else:
        return "No answer generated."

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
