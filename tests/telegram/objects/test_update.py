import pytest

from telegram.objects import Update


@pytest.fixture()
def parse_update_dict(dict_parser):
    return dict_parser(Update)


def test_empty_dict(parse_update_dict):
    with pytest.raises(TypeError, match='missing 1 required positional argument.*update_id') as exc_info:
        parse_update_dict({})


def test_empty_update(parse_update_dict):
    update = parse_update_dict(dict(update_id=1))
    assert update.update_id == 1
    assert update.message is None
    assert update.edited_message is None
    assert update.channel_post is None
    assert update.edited_channel_post is None


def test_update_with_message(parse_update_dict):
    update_dict = {
        "update_id": 10000,
        "message": {
            "message_id": 1365,
            "date": 1441645532,
            "chat": {
                "id": 1111111,
                "type": "private",
                "username": "Testusername",
                "first_name": "Test Firstname",
                "last_name": "Test Lastname",
            },
            "from": {
                "last_name": "Test Lastname",
                "id": 1111111,
                "first_name": "Test Firstname",
                "username": "Testusername",
            },
            "text": "/start"
        },
    }
    update = parse_update_dict(update_dict)
    assert update.update_id == 10000
    assert update.message is not None
    assert update.message.message_id == 1365
    assert update.message.date == 1441645532
    assert update.message.chat is not None
    assert update.message.chat.id == 1111111
    assert update.message.chat.type == 'private'
    assert update.message.chat.username == 'Testusername'
    assert update.message.chat.first_name == 'Test Firstname'
    assert update.message.chat.last_name == 'Test Lastname'
    assert update.message.from_user is None  # FIXME
    assert update.message.text == '/start'
    assert update.edited_message is None
    assert update.channel_post is None
    assert update.edited_channel_post is None
