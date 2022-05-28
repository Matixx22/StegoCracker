from src.getdata.html.get_tags_letters import get_data as html_get_tags
from src.checkdata.pdf import check_data as check_pdf


# Check html
def test_check_pdf_html():
    data = check_pdf(html_get_tags('tests/res/html/pdf_in_html.html'), 'tests/res/')

    assert data[0] is True

    # with open('tests/res/hidden/hidden.pdf', 'r') as file:
    #     assert file.read() in data[1]


# Check lsb
def test_check_pdf_lsb():
    pass


# Check icmp
def test_check_pdf_icmp():
    pass
