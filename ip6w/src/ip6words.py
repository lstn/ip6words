import sys
import os

from ip6w.src.iwords import dill_words
from ip6w.src import ip_handling

def conv_to_words(words, ip_to_process, explode_results):
    ip = ip_handling.to_words.ipv6_arrayize(ip_to_process)

    ipwords = ip_handling.to_words.ip_to_words_arr(ip, words)
    ipwords = ip_handling.to_words.compress_words(ipwords)

    if explode_results:
        ipwords = ip_handling.to_words.explode_words(ipwords)

    return ip_handling.to_words.words_arr_to_str(ipwords)

def conv_to_ipv6(words, ip_to_process, explode_results):
    ip = ip_handling.to_ipv6.ip6words_arrayize(ip_to_process)
    ip = ip_handling.to_words.explode_words(ip)

    iphex = ip_handling.to_ipv6.words_to_ipv6_arr(ip, words)
    return ip_handling.to_ipv6.iphex_arr_to_str(iphex, explode_results)

def load_words():
    return dill_words(ip_handling.iutils.get_ipv6_word_possibilities() + 1)

def main(argv):
    ip_to_process, convert_to, explode_results = parse_args(argv[1:])
    words = load_words()

    if convert_to == "words":
        res = conv_to_words(words, ip_to_process, explode_results)
    elif convert_to == "ipv6":
        res = conv_to_ipv6(words, ip_to_process, explode_results)
    else:
        raise Exception("Could not determine the type of IP being queried")
    print(res)
    return res
    
def parse_args(args):
    cmd_opts = {
        "-d": _delete_dill,
        "-u": disp_usage,
        "-h": disp_help,
        "-e": lambda: True,
    }
    explode_results = False
    if(len(args) == 1):
        cmdarg = cmd_opts.get(args[0], None)
        if cmdarg is None:
            ip_to_process = args[0]
        else:
            cmdarg()
            sys.exit()
    elif(len(args) == 2):
        cmdarg = cmd_opts.get(args[0], disp_usage)
        if cmdarg() is False:
            sys.exit()
        ip_to_process = args[1]
        if args[0] == "-e":
            explode_results = True
    else:
        disp_usage()
        sys.exit(1)

    convert_to = ip_handling.iutils.get_conversion_type(ip_to_process)

    return ip_to_process, convert_to, explode_results

def disp_usage():
    print("Usage:\n\tpython {} {} {}".format(sys.argv[0], "([-h] | [-d] | [-u] | [-e])", "(<ip6words-address-to-convert> | <ipv6-to-convert>)"))
    return False

def disp_help():
    disp_usage()
    print("\t [-h] ~ This dialog")
    print("\t [-u] ~ The usage dialog")
    print("\t [-d] ~ Delete the dilled (pickled) word list in order to regenerate it before executing")
    print("\t [-e] ~ Explode the results instead of compressing them")
    return False

def _delete_dill(fname="words.dill"):
    os.path.join(os.path.dirname(os.path.realpath(__file__)), fname)
    try:
        if os.path.isfile(fname):
            os.remove(fname)
        return True
    except:
        raise Exception("Error while checking/removing dill file")

if __name__ == "__main__": main(sys.argv)