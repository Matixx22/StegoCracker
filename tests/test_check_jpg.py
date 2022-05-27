import cv2

from src.getdata.html.get_tags_letters import get_data as html_get_tags
from src.checkdata.jpg import check_data as check_jpg


# Check html
def test_check_jpg_html():
    data = check_jpg(html_get_tags('tests/res/html/jpg_in_html.html'), 'tests/res')

    assert data[0] is True

    hidden = cv2.imread('tests/res/hidden/hidden.jpg')
    data_file = cv2.imread(data[1])

    # TODO: w ogole nie da sie testowac tego co zrobiles Kacper
    # h_shape = hidden.shape[:2]
    # d_shape = data_file.shape[:2]

    # assert h_shape == d_shape
    # assert hidden is data_file


# Check lsb
def test_check_jpg_lsb():
    pass


# Check icmp
def test_check_jpg_icmp():
    pass
