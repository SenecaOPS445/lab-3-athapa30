#!/usr/bin/env python3
'''Lab 3 Part 4 - Disk Space Check'''


import subprocess

def free_space():
    
    output = subprocess.check_output("df -h | grep '/$' | awk '{print $4}'", shell=True)
    
    
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    
    print(free_space())
