from voluptuous import PREVENT_EXTRA, Schema


register_user = Schema(
    {
        "id": int,
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

login_user = Schema(
    {
        'token': str
    }
)

create_user = Schema(
    {
        'name': str,
        'job': str,
        'id': str,
        'createdAt': str
    },
)

register_unsuccessful_user = Schema(
    {
        "error": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_user = Schema(
    {
        'name': str,
        'job': str,
        'updatedAt': str
    }
)