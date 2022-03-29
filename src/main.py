from getdata import icmp_get_data
from getdata import image_get_lsb
from getdata import html_get_lower_letters
from getdata import html_get_upper_letters

from checkdata import check_hash
from checkdata import check_jpg
from checkdata import check_pdf
from checkdata import check_txt

"""
In main script there will be implemented multithreading and option parser for different crack methods
"""

"""
But for now it's showing how to use getdata and checkdata packages
"""


def find_steg(source):
    find_hash = check_hash(source)
    if find_hash[0]:
        print("Found Hash " + find_hash[1])
        return "Found Hash " + find_hash[1]

    find_jpg = check_jpg(source)
    if find_jpg[0]:
        print("Found JPG. New file location: " + find_jpg[1])
        return "Found JPG. New file location: " + find_jpg[1]

    find_pdf = check_pdf(source)
    if find_pdf[0]:
        print("Found PDF. New file location: " + find_pdf[1])
        return "Found PDF. New file location: " + find_pdf[1]

    find_txt = check_txt(source)
    if find_txt[0]:
        print("Found text: " + find_txt[1])
        return "Found text: " + find_txt[1]

    return None


if __name__ == '__main__':
    html_filename = "./example.html"
    pcap_filename = "./example.pcap"
    img_filename = "./example.jpg"

    find_steg(html_get_lower_letters(html_filename))
    find_steg(html_get_upper_letters(html_filename))
    find_steg(icmp_get_data(pcap_filename))
    find_steg(image_get_lsb(img_filename))
