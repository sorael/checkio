def checkio(data):
    # replace this for solution
    l_ip_b = []
    for ip in data:
        l_ip_b.append(''.join([bin(int(i))[2:].rjust(8, '0') for i in ip.split('.')]))

    mask_length = 0
    while mask_length <= 32:
        if len(set([i[mask_length] for i in l_ip_b])) == 1:
            mask_length += 1
        else:
            break

    summary_bin = l_ip_b[0][:mask_length] + '0'*(32-mask_length)
    ip = '.'.join([str(int(summary_bin[i:i+8], 2)) for i in range(0, 32, 8)])
    return ip + '/' + str(mask_length)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
