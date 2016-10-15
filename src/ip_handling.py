import ipaddress

def get_osize():
    return 16

def get_iwlen():
    return 4

def get_ipv6_word_possibilities():
    return get_osize()**get_iwlen()

def ipv6_arrayize(ip_addr):
    ip = str(ipaddress.IPv6Address(ip_addr).exploded)
    ip_arr = ip.split(":")

    for i, word in enumerate(ip_arr):
        ip_arr[i] = int(word, get_osize())

    return ip_arr

def ip_to_words_arr(ip_arr, words_arr):
    if(len(words_arr) < get_ipv6_word_possibilities()):
        raise Exception("Not enough words")

    ipwords = [words_arr[iw] for iw in ip_arr]
    
    return ipwords

def words_arr_to_str(words_arr):
    return '.'.join(words_arr)