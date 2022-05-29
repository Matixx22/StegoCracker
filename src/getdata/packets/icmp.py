from scapy.all import rdpcap


def _data_from_icmp(icmp_packet):
    print(icmp_packet)


def get_data(filename) -> bytes:
    """
    Get data from Internet Control Message Protocol packet.
    Extracts every ICMP packet from pcap file.

    Args:
        filename (str): file contains ICMP packets (.pcap)

    Raises:
        TODO jak coś będzie

    Returns:
        data (bytes): Data extracted from packet

    """
    data = b''

    packets = rdpcap(filename)

    for packet in packets:
        if packet.haslayer("ICMP"):
            if packet["ICMP"].load != b'\x00':
                data = data + packet["ICMP"].load

    return data


if __name__ == '__main__':
    print(get_data("../../../resources/hidden/sample_icmp.pcapng"))
