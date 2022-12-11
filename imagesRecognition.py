"""
图片文字提取

"""

import os.path
from pprint import pprint
import json
from azure.cognitiveservices.vision.contentmoderator.models import Screen, OCR

TEXT_FOLDER = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "text_files")
from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
import azure.cognitiveservices.vision.contentmoderator.models
from msrest.authentication import CognitiveServicesCredentials


CONTENT_MODERATOR_ENDPOINT = "https://checklang.cognitiveservices.azure.com/"
subscription_key = "de74737edfd1481a8bcd28ff9e119d92"

client = ContentModeratorClient(
    endpoint=CONTENT_MODERATOR_ENDPOINT,
    credentials=CognitiveServicesCredentials(subscription_key)
)

IMAGE_LIST = [
    "https://img.51miz.com/Element/00/81/88/01/2ee2e354_E818801_d8b9322e.png",
    "https://ts1.cn.mm.bing.net/th/id/R-C.21472d02152d574348ad8411cf8de1ab?rik=EFyB%2fFePzqLivg&riu=http%3a%2f%2fimg.mm4000.com%2ffile%2fa%2fce%2fa331a51c57.jpg%3fdown&ehk=jvmhSo8RTrHkcgaxZ4dZqBRiPU%2bsrbHoOeW4byxWDK0%3d&risl=&pid=ImgRaw&r=0"
]


def images_recognition(url):
    evaluation = client.image_moderation.ocr_url_input(
        language="eng",
        content_type="application/json",
        data_representation="URL",
        value=url,
        cache_image=True,
    )
    assert isinstance(evaluation, OCR)
    print(evaluation.as_dict())
    return evaluation.text
