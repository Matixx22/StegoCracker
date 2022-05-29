from src.checkdata.exe import check_data as check_exe
from src.getdata.html.get_tags_letters import get_data as html_get_tags
from src.getdata.packets.icmp import get_data as icmp_get_data


# Check html
# TODO: make smaller exe or bigger html
# TODO: output path sometimes does not work
def test_check_exe_html():
    # pass
    data = check_exe(html_get_tags('tests/res/html/exe_in_html.html'), 'tests/res/')

    assert data[0] is True


# Check lsb
# def test_check_exe_lsb():
#     pass


# Check icmp
def test_check_exe_icmp():
    data = check_exe(icmp_get_data('tests/res/icmp/exe_in_icmp.pcapng'), 'tests/res/')

    assert data[0] is True
