import sys
import os

from iwords import dill_words
import ip_handling

def conv_to_words(words, ip_to_process):
    ip = ip_handling.to_words.ipv6_arrayize(ip_to_process)

    ipwords = ip_handling.to_words.ip_to_words_arr(ip, words)

    ipwords = ip_handling.to_words.compress_words(ipwords)
    # ip_handling.to_words.explode_words(cpr_wrds)

    ipstr = ip_handling.to_words.words_arr_to_str(ipwords)

    print(ipstr)
    return ipstr

def conv_to_ipv6(words, ip_to_process):
    ip = ip_handling.to_ipv6.ip6words_arrayize(ip_to_process)
    ip = ip_handling.to_words.explode_words(ip)

    iphex = ip_handling.to_ipv6.words_to_ipv6_arr(ip, words)
    ipstr = ip_handling.to_ipv6.iphex_arr_to_str(iphex)

    print(ipstr)
    return ipstr

def main(argv):
    ip_to_process, convert_to = parse_args(argv[1:])
    words = dill_words(ip_handling.iutils.get_ipv6_word_possibilities()+1)
    
    if convert_to == "words":
        return conv_to_words(words, ip_to_process)
    elif convert_to == "ipv6":
        return conv_to_ipv6(words, ip_to_process)
    else:
        raise Exception("Could not determine the type of IP being queried")
    
def parse_args(args):
    cmd_opts = {
        "-d": _delete_dill,
        "-u": disp_usage,
        "-h": disp_help,
    }
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
    else:
        disp_usage()
        sys.exit(1)

    convert_to = ip_handling.iutils.get_conversion_type(ip_to_process)

    return ip_to_process, convert_to

def disp_usage():
    print("Usage:\n\tpython {} {} {}".format(sys.argv[0], "([-h] | [-d] | [-u])", "(<ip6words-address-to-convert> | <ipv6-to-convert>)"))
    return False

def disp_help():
    disp_usage()
    print("\t [-h] ~ This dialog")
    print("\t [-u] ~ The usage dialog")
    print("\t [-d] ~ Delete the dilled (pickled) word list in order to regenerate it before executing")
    return False

def _delete_dill(fname="words.dill"):
    try:
        if os.path.isfile(fname):
            os.remove(fname)
        return True
    except:
        raise Exception("Error while checking/removing dill file")

if __name__ == "__main__": main(sys.argv)