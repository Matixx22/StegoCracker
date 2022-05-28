from src.getdata.html.get_tags_letters import get_data as html_get_tags
from src.getdata.packets.icmp import get_data as icmp_get_data
from src.checkdata.hash import check_data as check_hash
from src.checkdata.txt import check_data as check_txt


# Check html
# TODO: nie wiem czemu to nie dziala, a jak sie odpala z maina ten plik to dziala
def test_check_hash_html():
    data = check_txt(html_get_tags('tests/res/html/hash_in_html.html'))
    data_hash = check_hash(data[1])

    assert data_hash[0] is True

    with open('tests/res/hidden/hidden.hash', 'r') as file:
        assert file.read() in data_hash[1]


# Check lsb
def test_check_hash_lsb():
    pass


# Check icmp
def test_check_hash_icmp():
    data = check_txt(icmp_get_data('tests/res/icmp/hash_in_icmp.pcapng'))
    data_hash = check_hash(data[1])

    assert data_hash[0] is True

    with open('tests/res/hidden/hidden.hash', 'r') as file:
        assert file.read() in data_hash[1]
