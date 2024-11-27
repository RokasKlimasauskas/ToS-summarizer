import openai
from dotenv import load_dotenv
import os
from retrieve_tos_content import content

# Loading enviroment variables from .env file 
load_dotenv() 
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_text(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Using the 'gpt-3.5-turbo' model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

url = "https://my.nordaccount.com/legal/terms-of-service/"
url2 = "https://help.netflix.com/legal/termsofuse?locale=en&docType=termsofuse"

ToS_content = content(url)

prompt = f"""Review the Terms of Service, including the refund and billing policies, and provide a summary focusing on the following key points:
1. Confirm if subscriptions are set to auto-renew, and specify how to disable auto-renewal to avoid unexpected charges.
2. Detail the exact time frame and steps needed to request a refund, including how and where to submit the request.
3. Summarize any requirements for notifying the service of disputes or issues before initiating formal action.
4. Summarize the termination and suspension clauses, including conditions that could lead to suspension or termination.
5. Provide contact methods for support, including email addresses or other contact details I should use for assistance or to address issues.

Provide clear, actionable steps to avoid automatic charges and to remain eligible for refunds if needed.

{ToS_content}"""

summary = generate_text(prompt)

print(summary)

