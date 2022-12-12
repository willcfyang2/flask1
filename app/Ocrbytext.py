import os.path
from pprint import pprint
import time
from io import BytesIO
from random import random
import uuid

from azure.cognitiveservices.vision.contentmoderator.models import Screen

"""
正文提取
"""

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


def text_ocr():
    with open(os.path.join(TEXT_FOLDER, 'content_moderator_text_moderation.txt'), "rb") as text_fd:
        screen = client.text_moderation.screen_text(
            text_content_type="text/plain",
            text_content=text_fd,
            language="eng",
            autocorrect=True,
            pii=True
        )
        assert isinstance(screen, Screen)
        return str(screen.as_dict())