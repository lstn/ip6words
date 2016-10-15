# ip6words [![Pypi Version][pypi-version-badge]][pypi-version-link] [![Dependency CI][dependency-ci-badge]][dependency-ci-link] [![Apache 2 License][license-badge]][license-link]

Converts IPv6 addresses to and from a user friendly format using words.

#### Usage

<p align="center">
    <img src="https://raw.githubusercontent.com/lstn/ip6words/master/usage.gif" alt="Gif usage examples">
</p>

```bash
$ python ip6words.py -h
Usage:
        python ip6words.py ([-h] | [-d] | [-u]) (<ip6words-address-to-convert> | <ipv6-to-convert>)
         [-h] ~ This dialog
         [-u] ~ The usage dialog
         [-d] ~ Delete the dilled (pickled) word list in order to regenerate it before executing
```

#### Requirements

- Python 3.3+ (NOT tested at all on Python 2)
- nltk <sub>(*will download these packages on first run that doesn't use dill, download them yourself beforehand if you'd like to choose the download directory*)</sub>
 + words - <sub>*optional* ~ see note #3</sub>
 + brown - <sub>*optional* ~ see note #3</sub>
 + abc - <sub>*optional* ~ see note #3</sub>
 + inaugural - <sub>*optional* ~ see note #3</sub>
 + genesis - <sub>*optional* ~ see note #3</sub>
- dill


#### Notes

1. This is designed to have the same words always point to the same IP and vice versa. The only thing that
would alter this would be a change in the base nltk data, causing a shift in the frequency of words.
2. Included with this tool is a dilled (or pickled) word list. If you wish to re-generate that dill you
must delete the file or run using the \[-d] argument.
3. In practice, this means you will actually never have to download the nltk packages yourself if you never
use the \[-d] argument and thus always load the wordlist from the dill.

[pypi-version-badge]:	https://badge.fury.io/py/ip6words.svg
[pypi-version-link]:	https://pypi.python.org/pypi/ip6words/
[dependency-ci-badge]:	https://dependencyci.com/github/lstn/ip6words/badge
[dependency-ci-link]:	https://dependencyci.com/github/lstn/ip6words
[license-badge]:		https://img.shields.io/badge/license-Apache%202-blue.svg
[license-link]:			https://raw.githubusercontent.com/lstn/ip6words/master/LICENSE
