# -*- coding: utf-8 -*-

import time

correct_password = "8jf&2"
padding = "                    "
        
def check_password(pwd):
    pwd += padding
    correct_pwd_len = len(correct_password)
    for i in range(correct_pwd_len):
        time.sleep(0.000001)
        if pwd[i] != correct_password[i]:
            return "Wrong"
    return "Correct"