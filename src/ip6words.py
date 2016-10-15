import sys

from iwords import dill_words
import ip_handling

def main(argv):
    ip_to_process = parse_args(argv[1:])

    # print("Processing ip...")
    ip = ip_handling.ipv6_arrayize(ip_to_process)

    # print("Loading words...")
    words = dill_words(ip_handling.get_ipv6_word_possibilities()+1)

    # print("Converting ip...")
    ipwords = ip_handling.ip_to_words_arr(ip, words)
    ipstr = ip_handling.words_arr_to_str(ipwords)

    print(ipstr)
    return ipstr
    
def parse_args(args):
    ip_to_process = args[0]
    return ip_to_process

if __name__ == "__main__": main(sys.argv)