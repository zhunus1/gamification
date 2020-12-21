import json

import logging

from django.conf import settings

from django.utils import timezone

from rest_framework import exceptions, status
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from utils.encryption import encrypt, decrypt

from django.core.exceptions import ObjectDoesNotExist

from .models import User


logger = logging.getLogger(__name__)

class GamificationAuthentication(BaseAuthentication):

    TOKEN_PREFIX = 'Java'
    model = None

    @staticmethod
    def get_token_from_credentials(user):
        data = {
            'user_id': user.pk,
            'password': user.password,
            'created': str(timezone.now()),
        }
        b = json.dumps(data)
        token = encrypt(b.encode().hex(), settings.SECRET_KEY)
        return token

    @staticmethod
    def get_credentials_from_token(token):
        try:
            payload = bytes.fromhex(decrypt(token, settings.SECRET_KEY))
            data = json.loads(payload)
            user = User.objects.get(pk=data['user_id'],password=data['password'])
            return user,token
        except Exception:
            return None

    def authenticate(self, request):
        try:
            auth = get_authorization_header(request).decode().split()

            if not auth or auth[0] != GamificationAuthentication.TOKEN_PREFIX:
                return None

            user, token = GamificationAuthentication.get_credentials_from_token(auth[1])
            user.token = token
            if user is not None:
                return user, auth[1]
            return None
        except Exception as e:
            return None
