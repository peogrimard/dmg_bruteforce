#Author: Girish (z3nc1ph3r)
import os
import sys
import pexpect


target_dmg = raw_input("Enter taget dmg file path: ")

#file existance validation in if condition, when validated getting the file name out of path
if not (os.path.exists(target_dmg.strip()) and os.path.isfile(target_dmg.strip())):
    print "File doesn't exist"
    exit()
else:
    filename_w_ext = os.path.basename(target_dmg.strip())
    filename, file_extension = os.path.splitext(filename_w_ext)
    dmg_file_name = filename+file_extension


word_list = raw_input("Enter wordlist file path: ")
#file existance validation in if condition
if not (os.path.exists(word_list.strip()) and os.path.isfile(word_list.strip())):
    print "File doesn't exist"
    exit()
else:
    # reading wordlist file line by line and checking for correct passoword using hdiutil binary
    with open(word_list.strip()) as passwords:
        for line in passwords:
            child = pexpect.spawn('hdiutil verify '+target_dmg)
            i = child.expect([pexpect.EOF,pexpect.TIMEOUT, 'Enter password to access "'+dmg_file_name+'"'])
            child.sendline(line)
            child.expect(':')
            i = child.expect([pexpect.EOF,'hdiutil: verify failed - Authentication error'])
            if i == 0:
                print line.strip("\n") + " found :)"
                exit()
            else:
                print line.strip("\n") + " not working"
