import ipaddress
import re

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

        elif len(ip.split(".")) == 8:
            return "ipv6"

        __contains_alpha = lambda w: any(i.isalpha() for i in w)
        i = 0

        for word in ip.split("."):
            if not __contains_alpha(word):
                break
            i += 1
        if len(ip.split(".")) == i:
            return "ipv6"

        if len(ip.split(".")) == 4:
            raise Exception("Cannot convert IPv4 addresses!")

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

    def compress_words(ipwords):
        if len(ipwords) < 2 or len(ipwords) == len(set(ipwords)):
            return ipwords
        
        repeat_ranges = {}
        prev_val = None
        prev_i = None
        compressed = []

        for i, val in enumerate(ipwords):
            if prev_val == val:
                repeat_ranges[prev_i] = i
            else:
                repeat_ranges[i] = i
                prev_val = val
                prev_i = i
        
        for i, key in enumerate(repeat_ranges.keys()):
            if key == repeat_ranges[key]:
                compressed += [ipwords[key]]
            else:
                num_reps = repeat_ranges[key] - key + 1 # +1 due to index
                compressed += [ ipwords[key] + str(num_reps) ]

        return compressed
        
    def explode_words(ipwords):
        if len(ipwords) == 8:
            return ipwords

        __contains_digits = lambda w: any(i.isdigit() for i in w)
        compressed_idx = []
        to_explode = {}
        exploded = []

        for i, val in enumerate(ipwords):
            if __contains_digits(val):
                compressed_idx += [i]

        for idx in compressed_idx:
            j = ipwords[idx][-1]
            if j.isdigit():
                to_explode[idx] = int(j)
        
        for i in range(len(ipwords)):
            if i in to_explode.keys():
                exploded += [ipwords[i][:-1] for j in range(to_explode[i])]
            else:
                exploded += [ipwords[i]]

        return exploded


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
