# Grain-Predictor

you can add images and see what kind of grain it is

## working link:
curl --location --request POST 'https://predict.app.landing.ai/inference/v1/predict?endpoint_id=526f4ac4-6701-4d3f-867c-0066aa500028' \
     --header 'Content-Type: multipart/form-data' \
     --header 'apikey: YOUR_APIKEY' \
     --form 'file=@"YOUR_IMAGE"'
