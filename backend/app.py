from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

def extract_text_from_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script, style, nav, footer, aside tags
    for element_type in ["script", "style", "nav", "footer", "aside", "header", "form"]:
        for element in soup.find_all(element_type):
            element.decompose()

    # Get text from common content tags
    texts = []
    # More specific tags first
    for tag in soup.find_all(['article', 'main', 'div', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'span', 'td', 'th']):
        text_content = tag.get_text(separator=' ', strip=True)
        if text_content:
            texts.append(text_content)
    
    # Fallback if specific tags yield little
    if not texts:
        body = soup.find('body')
        if body:
            texts = [t.strip() for t in body.get_text(separator='\n', strip=True).split('\n') if t.strip()]


    # Remove excessive newlines and join
    # Filter out very short lines that are likely not content
    cleaned_texts = [text for text in texts if len(text.split()) > 3] # Heuristic: lines with more than 3 words
    if not cleaned_texts and texts: # if filtering removed everything, revert to less strict filtering
        cleaned_texts = [text for text in texts if len(text.strip()) > 10] # Heuristic: lines longer than 10 chars

    return "\n".join(cleaned_texts) if cleaned_texts else " ".join(t.strip() for t in soup.find_all(string=True) if t.strip())


@app.route('/api/process-url', methods=['POST'])
def process_url_route():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        
        # Check content type
        content_type = response.headers.get('Content-Type', '').lower()
        if 'text/html' not in content_type:
            return jsonify({'error': f'URL does not point to HTML content. Content-Type: {content_type}'}), 400

        extracted_text = extract_text_from_html_content(response.content)

        if not extracted_text.strip():
             return jsonify({'error': 'Could not extract meaningful text from the URL.'}), 500

        return jsonify({'text': extracted_text})
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error fetching URL {url}: {e}")
        return jsonify({'error': f'Failed to fetch URL: {str(e)}'}), 500
    except Exception as e:
        app.logger.error(f"Error processing URL {url}: {e}")
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    