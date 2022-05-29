from src.checkdata.txt import check_data as check_txt
from src.getdata.html.get_tags_letters import get_data as html_get_tags
from src.getdata.packets.icmp import get_data as icmp_get_data


# Check html
def test_check_txt_html():
    data = check_txt(html_get_tags('tests/res/html/txt_in_html.html'))

    assert data[0] is True

    with open('tests/res/hidden/hidden.txt', 'r') as file:
        assert file.read() in data[1]


# Check lsb
# def test_check_txt_lsb():
#     data = check_txt(image_get_lsb('tests/res/lsb/txt_in_jpg.jpg'))
#
#     assert data[0] is True
#
#     with open('tests/res/hidden/hidden2.txt', 'r') as file:
#         assert file.read() in data[1]


# Check icmp
def test_check_txt_icmp():
    data = check_txt(icmp_get_data('tests/res/icmp/txt_in_icmp.pcapng'))

    assert data[0] is True

    with open('tests/res/hidden/hidden.hash', 'r') as file:
        assert file.read() in data[1]

