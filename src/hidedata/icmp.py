from scapy.all import IP, ICMP, send


def hide_in_icmp(data, src_ip, dst_ip):
    data = bytearray(data)
    payload_length = 64
    counter = 0
    while True:
        if len(data) - (counter+1)*payload_length > 0:
            message = data[counter*payload_length:(counter+1)*payload_length]
        else:
            message = data[counter*payload_length:]
            break
        icmp = IP(src=src_ip, dst=dst_ip)/ICMP()/message
        send(icmp)
        counter = counter+1

    icmp = IP(src=src_ip, dst=dst_ip) / ICMP() / message
    send(icmp)


if __name__ == '__main__':
    src_ip = "1.1.1.1"
    dst_ip = "2.2.2.2"
    data = open("../../resources/sample.jpg", "rb").read()
    hide_in_icmp(data, src_ip, dst_ip)
