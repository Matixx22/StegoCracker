from src.getdata.html.get_tags_letters import get_data as html_get_tags
from src.checkdata.txt import check_data as check_txt


# Check html
def test_check_txt_html():
    data = check_txt(html_get_tags('tests/res/html/txt_in_html.html'))

    assert data[0] is True

    with open('tests/res/hidden/hidden.txt', 'r') as file:
        assert file.read() in data[1]


# Check lsb
def test_check_txt_lsb():
    pass


# Check icmp
def test_check_txt_icmp():
    pass

