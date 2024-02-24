#!/usr/bin/env python3
""" BasicAuth module """

import base64
from typing import Tuple, TypeVar, List
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the base64 encoded authorization header.

        Args:
            authorization_header (str): The authorization header.

        Returns:
            str: The base64 encoded authorization header.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decode a base64-encoded authorization header.

        Args:
            base64_authorization_header (str): The base64-encoded
                    authorization header.

        Returns:
            str: The decoded authorization header as a string,
                    or None if decoding fails.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            message_bytes = base64.b64decode(base64_authorization_header)
            return message_bytes.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts the username and password from a decoded base64
            authorization header.

        Args:
            decoded_base64_authorization_header (str): The decoded base64
                authorization header.

        Returns:
            tuple: A tuple containing the username and password extracted
                from the authorization header.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
                self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Retrieve a user object based on the provided credentials.

        Args:
            user_email (str): The email of the user.
            user_pwd (str): The password of the user.

        Returns:
            User: The user object if the credentials are valid, None otherwise.
        """
        if user_email is None:
            return None
        if not isinstance(user_email, str):
            return None
        if user_pwd is None:
            return None
        if not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        if not users:
            return
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user based on the provided request.

        Args:
            request (Request): The request object containing
                the authorization header.

        Returns:
            User: The user object corresponding to the provided
                credentials.
        """
        header = self.authorization_header(request)
        if header is None:
            return None
        base64_auth = self.extract_base64_authorization_header(header)
        if base64_auth is None:
            return None
        decoded_base64 = self.decode_base64_authorization_header(base64_auth)
        if decoded_base64 is None:
            return None
        user_credentials = self.extract_user_credentials(decoded_base64)
        if user_credentials is None:
            return None
        return self.user_object_from_credentials(*user_credentials)

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts the email and password from a decoded base64
            authorization header.

        Args:
            decoded_base64_authorization_header (str): The decoded base64
                authorization header.

        Returns:
            Tuple[str, str]: A tuple containing the email and password
                extracted from the header.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
