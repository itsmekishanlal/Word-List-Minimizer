#!/usr/bin/env python3
# https://github.com/itsmekishanlal/Word-List-Minimizer

import re
import argparse
import fileinput

# =====================================================================================================================


banner = """
@ # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # @
#                      <---- https://github.com/itsmekishanlal ---->                            #
#    __    __              _     __ _     _            _       _           _                    #
#   / / /\ \ \___  _ __ __| |/\// /(_)___| |_ /\//\/\ (_)_ __ (_)_ __ ___ (_)_______ _ __       #
#   \ \/  \/ / _ \| '__/ _` |/\/ / | / __| __|/\/    \| | '_ \| | '_ ` _ \| |_  / _ \ '__|      #
#    \  /\  / (_) | | | (_| | / /__| \__ \ |_  / /\/\ \ | | | | | | | | | | |/ /  __/ |         #
#     \/  \/ \___/|_|  \__,_| \____/_|___/\__| \/    \/_|_| |_|_|_| |_| |_|_/___\___|_|         #
#      by @itsmekishanlal                                                                  v1.0 #
@ # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # @
"""

# =====================================================================================================================


parser = argparse.ArgumentParser(
    prog = "Wolim",
    description = """This tool is used for fetching the specific password expiration form the multiple large wordlist
                     and make your specific password expiration wordlist for Brute-force. """

)

parser.add_argument(
    "wordlist",
    type = str,
    metavar = "Wordlist",
    action = "store",
    nargs = "+",
    help = "It takes list of wordlist separated by spaces OR one wordlist"
)

parser.add_argument(
    "string",
    type = str,
    metavar = "String",
    help = "It takes the password string "
)

parser.add_argument(
    "-o",
    "--output",
    type = str,
    metavar = "",
    default = "output.txt",
    help = "This is for the output file in which you wanna get the output."
)

parser.add_argument(
    "-v",
    "--version",
    action = "version",
    version = "%(prog)s : v1.0"
)

args = parser.parse_args()

# =====================================================================================================================


# password compression
def pass_comp(password, inpt_str):
    # convert simple string to byte string because we are reading file in bytes
    byte_string = inpt_str.encode()
    # iterate password list and find the pattern
    for buffer in password:
        pattern = re.findall(byte_string, buffer)
        # pattern returns the list so to compare the list element here i used the for loop
        for passwd in pattern:
            if byte_string == passwd:
                yield buffer

# =====================================================================================================================


def main(wordlist,  string, output):
    try:
        # Here I've used fileinput library for reading multiple files
        with fileinput.input(files = wordlist, mode = "rb") as wrdlist:
    
            # for GUI
            print("[+] Reading The " + str(wordlist) + " File...")
            
            # we are reading the file and store the passwords in the passwords list
            passwords = []
            for lines in wrdlist:
                passwords.append(lines)

            # for GUI
            print("[+] Finding The Match Of [ " + string + " ] From " + str(wordlist) + ".")
            
            # passing the passwords list and the string or expression
            opt_lst = pass_comp(password = passwords, inpt_str = string)
            
            with open(output, "ab") as outfile:
    
                # for GUI
                print("[+] Writing The [ " + output + " ] File...")
                
                # Here I've sed SET Data Structure for Uniqueness
                password_set = set()
                
                # Reading the opt_lst and add into password_set
                for line in opt_lst:
                    password_set.add(line)
                    
                # printing the set elements in the output file
                for characters in password_set:
                    outfile.write(characters)
                
                # for GUI
                print("[+] Successfully Written The [ " + output + " ] File. ")
                print("[+] Thanks For Using This Tool !!")
                
                outfile.close()
            
            wrdlist.close()
            
    except FileNotFoundError:
        # For Error Handling
        print("[!] 404 File Not Found !!!")

# =====================================================================================================================


if __name__ == '__main__':
    print(banner)
    main(wordlist = args.wordlist, string = args.string, output = args.output)
