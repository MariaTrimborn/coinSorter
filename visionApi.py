import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd
import tiltapi

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'coin.json'

client = vision_v1.ImageAnnotatorClient()

FILE_NAME = 'front.png'
FOLDER_PATH = r'C:\Users\maria\OneDrive\Documents\g_v'

with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
    content = image_file.read()

image = vision_v1.types.Image(content = content)

response = client.text_detection(image = image)
texts = response.text_annotations
df = pd.DataFrame(columns=['locale', 'description'])
for text in texts:
    df = df.append(
        dict(
        locale = text.locale,
        description = text.description
        ), 
        ignore_index=True
    )

date = df['description'][0]

res = [int(i) for i in date.split() if i.isdigit()]

res2 = str(res)[1:-1]

print("The date of this penny is: " + res2)
import predict
