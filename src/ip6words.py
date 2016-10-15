import sys

from iwords import dill_words
import ip_handling

def conv_to_words(words, ip_to_process):
    # print("Processing ip...")
    ip = ip_handling.ipv6_arrayize(ip_to_process)

    # print("Converting ip...")
    ipwords = ip_handling.ip_to_words_arr(ip, words)
    ipstr = ip_handling.words_arr_to_str(ipwords)

    print(ipstr)
    return ipstr

def conv_to_ipv6(words, ip_to_process):
    # print("Processing ip...")
    ip = ip_handling.ip6words_arrayize(ip_to_process)

    # print("Converting ip...")
    iphex = ip_handling.words_to_ipv6_arr(ip, words)
    ipstr = ip_handling.iphex_arr_to_str(iphex)

    print(ipstr)
    return ipstr

def main(argv):
    ip_to_process, convert_to = parse_args(argv[1:])
    words = dill_words(ip_handling.get_ipv6_word_possibilities()+1)
    
    if convert_to == "words":
        return conv_to_words(words, ip_to_process)
    elif convert_to == "ipv6":
        return conv_to_ipv6(words, ip_to_process)
    else:
        raise Exception("Could not determine the type of IP being queried")
    
def parse_args(args):
    ip_to_process = args[0]
    convert_to = ip_handling.get_conversion_type(ip_to_process)

    return ip_to_process, convert_to

if __name__ == "__main__": main(sys.argv)