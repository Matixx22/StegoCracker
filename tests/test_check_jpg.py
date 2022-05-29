from src.checkdata.jpg import check_data as check_jpg
from src.getdata.html.get_tags_letters import get_data as html_get_tags
from src.getdata.packets.icmp import get_data as icmp_get_data


# Check html
def test_check_jpg_html():
    data = check_jpg(html_get_tags('tests/res/html/jpg_in_html.html'), 'tests/res')

    assert data[0] is True


# Check lsb
# def test_check_jpg_lsb():
#     assert False


# Check icmp
def test_check_jpg_icmp():
    data = check_jpg(icmp_get_data('tests/res/icmp/jpg_in_icmp.pcapng'), 'tests/res')

    assert data[0] is True
