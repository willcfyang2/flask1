from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials


subscription_key = "3cbf56ac028f4a738d18f17bfe488ef1"
endpoint = "https://comserver.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


def ObjectRecognition(url):
    result = computervision_client.detect_objects(url)
    try:
        data = []
        ocr = result.objects[0]
        data.append(ocr.object_property)
        if ocr.parent:
            while 1:
                try:
                    ocr = ocr.parent
                    data.append(ocr.object_property)
                except Exception as e:
                    break
        return data
    except Exception as e:
        return "this objects is not recognition"



