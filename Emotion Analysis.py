import requests

url = "https://facial-emotion-recognition.p.rapidapi.com/cloudVision/facialEmotionRecognition"

querystring = {"source":"https://images.unsplash.com/photo-1527631120902-378417754324?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80","sourceType":"url"}

payload = "{\r\n    \"source\": \"https://images.unsplash.com/photo-1527631120902-378417754324?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80\",\r\n    \"sourceType\": \"url\"\r\n}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "8671a96a61msh86565f63e6a7c81p1911d5jsnc641b6e93b35",
    'x-rapidapi-host': "facial-emotion-recognition.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)