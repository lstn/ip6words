import ipaddress

class iutils:
    def get_osize():
        return 16

    def get_iwlen():
        return 4

    def get_ipv6_word_possibilities():
        return iutils.get_osize()**iutils.get_iwlen()
    
    def get_conversion_type(ip):
        if len(ip.split(":")) > 1 or ip[:2] == "::":
            if len(ip.split(":")) < 2 and ip[:2] == "::":
                return "words"
            elif len(ip.split(":")) != 8 and len(ip.split(":")) > 0 and "::" in ip:
                return "words"
            elif len(ip.split(":")) == 8:
                return "words"
        
        elif len(ip.split(".")) == 4:
            raise Exception("Cannot convert IPv4 addresses!")
        elif len(ip.split(".")) == 8:
            return "ipv6"

        return None


class to_words:
    def ipv6_arrayize(ip_addr):
        ip = str(ipaddress.IPv6Address(ip_addr).exploded)
        ip_arr = ip.split(":")

        for i, word in enumerate(ip_arr):
            ip_arr[i] = int(word, iutils.get_osize())

        return ip_arr

    def ip_to_words_arr(ip_arr, words_arr):
        if(len(words_arr) < iutils.get_ipv6_word_possibilities()):
            raise Exception("Not enough words")

        ipwords = [words_arr[iw] for iw in ip_arr]
        
        return ipwords
    
    def words_arr_to_str(words_arr):
        return '.'.join(words_arr)


class to_ipv6:
    def ip6words_arrayize(ip_addr):
        ip_arr = ip_addr.split(".")

        return ip_arr

    def words_to_ipv6_arr(ip_arr, words_arr):
        if(len(words_arr) < iutils.get_ipv6_word_possibilities()):
            raise Exception("Not enough words")
        def get_wkey(word):
            for i, value in enumerate(words_arr):
                if word == value:
                    return i
            raise Exception("Could not find word in words array")
        
        ipdec = []
        iphex = []
        
        for ipw in ip_arr:
            ipdec += [get_wkey(ipw)]
        for ipd in ipdec:
            iphex += [hex(ipd).split('x')[1]]
        
        return iphex

    def iphex_arr_to_str(iphex_arr):
        iphex = ':'.join(iphex_arr)
        iphex = str(ipaddress.IPv6Address(iphex).compressed)
        return iphex
