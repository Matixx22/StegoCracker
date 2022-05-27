from src.getdata.html.get_tags_letters import get_data as html_get_tags
from src.checkdata.hash import check_data as check_hash


# Check html
# TODO: nie wiem czemu to nie dziala, a jak sie odpala z maina ten plik to dziala
def test_check_hash_html():
    data = check_hash(html_get_tags('tests/res/html/hash_in_html.html'))

    assert data[0] is True

    with open('tests/res/hidden/hidden.hash', 'r') as file:
        assert file.read() in data[1]


# Check lsb
def test_check_hash_lsb():
    pass


# Check icmp
def test_check_hash_icmp():
    pass
