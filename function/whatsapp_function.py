import requests
from utils.constants import Constants

def send_whatsapp_message(data:list):
    try:
        url = Constants.whatsapp_url
        
        headers = {
            "Authorization": Constants.whatsapp_at,  # Replace with your Facebook Graph API access token
            "Content-Type": "application/json",
        }
        message = data[1]
        to = data[0]

        payload = {
            "messaging_product": "whatsapp",
            "to": "91" + to,  # Replace with the recipient's WhatsApp number
            "type": "template",
            "template": {
                "name": message,
                "language": {
                    "code": "en_US"
                }
            }
        }
        print(payload,"jdnckjcndkcsnkjcd")
        response = requests.post(url, headers=headers, json=payload)
        
        # Check the response status code
        if response.status_code == 200:
            print("Message sent successfully!")
            return ("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(response.text)  # Print the response content for debugging
    except Exception as e:
        print(f"An error occurred: {e}")



