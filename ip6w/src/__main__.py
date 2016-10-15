import sys
import ip6w.src.ip6words

def main(args=None):
    if args is None:
        args = sys.argv

    ip6w.src.ip6words.main(args)
    sys.exit()

if __name__ == "__main__":
    main()