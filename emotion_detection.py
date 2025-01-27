import requests

# Define the emotion detector function
def emotion_detector(text_to_analyze):
    # API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Input JSON
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    try:
        # Send a POST request
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        # Return the 'text' attribute of the response
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
