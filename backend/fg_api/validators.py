from rest_framework import serializers

from users.constants import FORBIDDEN_USERNAMES


def is_forbidden_names(username):
    return username.lower() in [name.lower() for name in FORBIDDEN_USERNAMES]


def validate_new_username(username):
    if is_forbidden_names(username):
        raise serializers.ValidationError(
            f'Использовать имя: {username} запрещено'
        )
    return username
