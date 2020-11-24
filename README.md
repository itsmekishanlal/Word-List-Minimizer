# Word-List-Minimizer

```sh
@ # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # @
#                           <---- https://github.com/itsmekishanlal ---->                           #
#   __          __           _ /\/|      _     _  /\/|_  __ _       _           _                   #
#   \ \        / /          | |/\/ |    (_)   | ||/\/  \/  (_)     (_)         (_)                  #
#    \ \  /\  / /__  _ __ __| |  | |     _ ___| |_  | \  / |_ _ __  _ _ __ ___  _ _______ _ __      #
#     \ \/  \/ / _ \| '__/ _` |  | |    | / __| __| | |\/| | | '_ \| | '_ ` _ \| |_  / _ \ '__|     #
#      \  /\  / (_) | | | (_| |  | |____| \__ \ |_  | |  | | | | | | | | | | | | |/ /  __/ |        #
#       \/  \/ \___/|_|  \__,_|  |______|_|___/\__| |_|  |_|_|_| |_|_|_| |_| |_|_/___\___|_|        #
#        by @itsmekishanlal                                                                    v1.0 #
@ # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # @
```

[![Python Version](https://img.shields.io/badge/python-3.9-blue?style=for-the-badge&logo=python)](https://github.com/EONRaider/Packet-Sniffer/)
[![Open Source? Yes!](https://img.shields.io/badge/Open%20Source%3F-Yes!-green?style=for-the-badge&logo=appveyor)](https://github.com/EONRaider/Packet-Sniffer/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](https://github.com/EONRaider/Packet-Sniffer/blob/master/LICENSE)

[![Reddit](https://img.shields.io/reddit/user-karma/combined/itsmekishanlal?style=flat-square&logo=reddit)](https://www.reddit.com/user/itsmekishanlal)
[![Twitter](https://img.shields.io/twitter/follow/itsmekishanlal?style=flat-square&logo=twitter)](https://twitter.com/intent/follow?screen_name=itsmekishanlal)

> ## **Description**

This tool is pretty straight-forward as name the suggest **Word-List-Minimizer** in short **Wolim**.

It's simply used to fetch the specific *password* expiration form the large wordlists to
make your short/personalized wordlist with specific *password* expiration.

* ## **Why I Create This Tool**

     When we are *brute-forcing* any *passwords* we need a wordlist, as we know that the wordlist are very large and takes too much time or sometimes we have 2-3 large wordlist which contains too many *passwords* and we don't need that much *passwords* and don't have that much time to do that so I think don't we make one tool which will fetch all the needed *passwords* from all of the wordlist and make a new wordlist which contains specific *password* expiration and also "make one subset of all that wordlist/make one mini-wordlist" in order to make our *password* cracking ***easier*** and ***faster***.

> ## **Installation For GNU / Linux & Other Systems**

* **Dependencies :-** I have used the library which comes with python by default in case you don't have then you can install through the below command

```sh
    user@host:~/DIR$ pip install re && pip install fileinput && pip install argparse
```

* Simply clone this repository with `git clone` and execute the `Wolim.py`
file as described in the following `Usage` section.

```sh
    user@host:~/DIR$ git clone https://github.com/itsmekishanlal/Word-List-Minimizer.git
```

> ## **Usage**

```sh
usage: Wolim [-h] [-o] [-v] Wordlist [Wordlist ...] String

This tool is used for fetching the specific password expiration form the multiple large wordlist and make your specific password expiration wordlist for Brute-force.

positional arguments:
  Wordlist        It takes list of wordlist separated by spaces OR one wordlist
  String          It takes the password string

optional arguments:
  -h, --help      show this help message and exit
  -o , --output   This is for the output file in which you wanna get the output.
  -v, --version   show program's version number and exit
```

> ## **Running The Tool**

* Here I took `Two` wordlist `rockyou.txt` and `EvilGhost.txt`. you can take as many as you want or only one it's totally fine.
* I wanna fetch that password which contains the word expiration `hacker` in it.
* For this execute the following command in your terminal or powershell.

```sh
  user@host:~/DIR$ python3 Wolim.py rockyou.txt EvilGhost.txt hacker
```

* **NOTE :**  Default output file is "output.txt".
* If you want to store your output in your specific file. you need to add `-s` flag with `your-output-file-name.txt` extension.
* Here I stored my output in hacker-list.txt file.

```sh
  user@host:~/DIR$ python3 Wolim.py rockyou.txt EvilGhost.txt hacker -s hacker-list.txt
```

> ## **Output sample captured during execution:**

```sh

@ # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # @
#                      <---- https://github.com/itsmekishanlal ---->                            #
#    __    __              _     __ _     _            _       _           _                    #
#   / / /\ \ \___  _ __ __| |/\// /(_)___| |_ /\//\/\ (_)_ __ (_)_ __ ___ (_)_______ _ __       #
#   \ \/  \/ / _ \| '__/ _` |/\/ / | / __| __|/\/    \| | '_ \| | '_ ` _ \| |_  / _ \ '__|      #
#    \  /\  / (_) | | | (_| | / /__| \__ \ |_  / /\/\ \ | | | | | | | | | | |/ /  __/ |         #
#     \/  \/ \___/|_|  \__,_| \____/_|___/\__| \/    \/_|_| |_|_|_| |_| |_|_/___\___|_|         #
#      by @itsmekishanlal                                                                  v1.0 #
@ # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # @

[+] Reading The ['rockyou.txt', 'EvilGhost.txt'] File...
[+] Finding The Match Of [ hacker ] From ['rockyou.txt', 'EvilGhost.txt'].
[+] Writing The [ hacker-list.txt ] File...
[+] Successfully Written The [ hacker-list.txt ] File.
[+] Thanks For Using This Tool !!
```
