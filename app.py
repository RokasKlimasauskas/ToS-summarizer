from flask import Flask, request, render_template
from retrieve_tos_content import content
from openai_utils import generate_text
from chromedriver_manager import ChromeDriverManager  # added new line
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

# Initialize ChromeDriver when the app starts
driver_manager = ChromeDriverManager()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    tos_content = content(url)
    
    prompt = f"""Review the Terms of Service, including the refund and billing policies, and provide a summary focusing on the following key points:
1. Confirm if subscriptions are set to auto-renew, and specify how to disable auto-renewal to avoid unexpected charges.
2. Detail the exact time frame and steps needed to request a refund, including how and where to submit the request.
3. Summarize any requirements for notifying the service of disputes or issues before initiating formal action.
4. Summarize the termination and suspension clauses, including conditions that could lead to suspension or termination.
5. Provide contact methods for support, including email addresses or other contact details I should use for assistance or to address issues.

Provide clear, actionable steps to avoid automatic charges and to remain eligible for refunds if needed.

{tos_content}"""
    
    summary = generate_text(prompt)
    
    return render_template('summary.html', summary=summary)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    driver_manager.close()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True)
