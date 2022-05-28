from src.getdata.html.get_tags_letters import get_data as html_get_tags
from src.checkdata.exe import check_data as check_exe


# Check html
# TODO: make smaller exe or bigger html
# TODO: output path sometimes does not work
def test_check_exe_html():
    # pass
    data = check_exe(html_get_tags('tests/res/html/exe_in_html.html'), 'tests/res/')

    assert data[0] is True

    # with open('tests/res/hidden/hidden.exe', 'rb') as hidden, open(data[1], 'rb') as data_file:
    #     check = True
    #     while byte := hidden.read(1):
    #         if byte != data_file.read(1):
    #             check = False
    #
    #     assert check is True



# Check lsb
def test_check_exe_lsb():
    pass


# Check icmp
def test_check_exe_icmp():
    pass
