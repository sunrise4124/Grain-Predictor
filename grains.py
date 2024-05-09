from PIL import Image
from landingai.predict import Predictor
# Enter your API Key
endpoint_id = "526f4ac4-6701-4d3f-867c-0066aa500028"
api_key = "FILL_YOUR_API_KEY"
# Load your image
image = Image.open("image.png")
# Run inference
predictor = Predictor(endpoint_id, api_key=api_key)
predictions = predictor.predict(image)
