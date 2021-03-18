# -*- coding: utf-8 -*-

from django.conf import settings

from rest_framework import authentication
from rest_framework.exceptions import NotAuthenticated

from jose.exceptions import ExpiredSignatureError

from keycloak.keycloak_openid import KeycloakOpenID


class KeepsAuthentication(authentication.TokenAuthentication):

    def __init__(self):
        self._config = getattr(settings, 'KEYCLOAK_CONFIG')

        # Read configurations
        try:
            self._server_url = self._config['KEYCLOAK_SERVER_URL']
            self._client_id = self._config['KEYCLOAK_CLIENT_ID']
            self._realm = self._config['KEYCLOAK_REALM']
        except KeyError as e:
            raise Exception("KEYCLOAK_SERVER_URL, KEYCLOAK_CLIENT_ID or KEYCLOAK_REALM not found.")

        self._client_secret_key = self._config.get('KEYCLOAK_CLIENT_SECRET_KEY', None)
        self._client_public_key = self._config.get('KEYCLOAK_CLIENT_PUBLIC_KEY', None)

        # Create Keycloak instance
        self._keycloak = KeycloakOpenID(server_url=self._server_url,
                                        client_id=self._client_id,
                                        realm_name=self._realm,
                                        client_secret_key=self._client_secret_key,
                                        verify=False)

    def authenticate(self, request):
        # Decode token and set request.user

        if self._skip_urls(request):
            return None, None

        user = self._get_token_info(request)
        user['client_id'] = self._get_profile(request)

        return user, None

    def _get_token_info(self, request):
        """ Decode token """

        # Options check token
        options = {"verify_signature": True, "verify_aud": False, "exp": True}

        # JWT not found
        if 'HTTP_AUTHORIZATION' not in request.META:
            raise NotAuthenticated("HTTP_AUTHORIZATION not found in the request")

        jwt = request.META.get('HTTP_AUTHORIZATION')

        try:
            token_info = self._keycloak.decode_token(jwt, key=self._client_public_key, options=options)
        except ExpiredSignatureError:
            options["verify_exp"] = False
            token_info = self._keycloak.decode_token(jwt, key=self._client_public_key, options=options)

            if "offline_access" in token_info['realm_access']['roles']:
                return token_info
            else:
                raise ExpiredSignatureError("Login expired")

        return token_info

    @staticmethod
    def _get_profile(request):
        return request.META.get('HTTP_X_CLIENT') or None

    @staticmethod
    def _skip_urls(request):
        if '/docs' in request.path or '/swagger' in request.path or '/redoc' in request.path:
            return True
        return False
