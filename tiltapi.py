import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd
from google.cloud import automl


def test():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'coin.json'
    
    project_id = "coin-sorter-308723"
    model_id = "ICN2963221220251664384"
    file_path = "front.png"

    prediction_client = automl.PredictionServiceClient()

        # Get the full path of the model.
    model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)

        # Read the file.
    with open(file_path, "rb") as content_file:
        content = content_file.read()

    image = automl.Image(image_bytes=content)
    payload = automl.ExamplePayload(image=image)

        # params is additional domain-specific parameters.
        # score_threshold is used to filter the result
        # https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictrequest
    params = {"score_threshold": "0.8"}

    request = automl.PredictRequest(name=model_full_id, payload=payload, params=params)

    response = prediction_client.predict(request=request)
    
    for result in response.payload:
        result.display_name
        # [END automl_vision_object_detection_predict]

    test.penny_tilt = result.display_name
    
    
    if test.penny_tilt == "tilt":
        test.penny_tilt = True
        import flipcoin
        flipcoin.flip()
        
    if test.penny_tilt == "notilt":
        test.penny_tilt = False

    

test()
while test.penny_tilt == True:
    test()

