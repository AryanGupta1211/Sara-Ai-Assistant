import cv2
import base64
from dotenv import load_dotenv, find_dotenv
from groq import Groq

_= load_dotenv(find_dotenv())

def capture_image() -> str:
    """ Capture an image from  the default webcam, resize and encode it as base64."""
    for idx in range(4):
        cap = cv2.VideoCapture(idx, cv2.CAP_DSHOW)
        if cap.isOpened():
            for _ in range(10):
                cap.read()
            ret, frame = cap.read()
            cap.release()
            if not ret:
                continue
            cv2.imwrite("sample.jpg", frame)
            ret, buf = cv2.imencode('.jpg', frame)
            if ret:
                return base64.b64encode(buf).decode('utf-8')
    raise RuntimeError("Could not find the webcam.")
    

def analyze_image_with_query(query: str) -> str:
    """
    Expects a string with 'query'
    Captures the image and sends the query and image to model vision chat API and return analysis.
    """
    img_64 = capture_image()
    model = "meta-llama/llama-4-maverick-17b-128e-instruct"
    
    if not query or not img_64:
        return "Error: 'Query' and 'Image' are required."
    
    client = Groq()
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_64}"
                    },
                },
            ],
        }
    ]
    
    chat_complition = client.chat.completions.create(
        messages=messages,
        model=model
    )
    
    return chat_complition.choices[0].message.content


# query="What is in my hand?"
# print(analyze_image_with_query(query))