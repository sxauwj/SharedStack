# -*- coding: utf-8 -*-

import numpy as np


class SharedStack(object):
    """OneArrayToTwoStack"""

    def __init__(self, maxsize):
        """
        :param maxsize: Array length
        """
        self.maxsize = maxsize
        self.items = [None for i in range(maxsize)]
        self.items = np.array(self.items)
        self.lpoint = 0
        self.rpoint = maxsize - 1

    def push(self, num, l_or_r):
        if (self.lpoint > self.rpoint):
            return "Stack Is Full"
        elif l_or_r == 'l':
            self.items[self.lpoint] = num
            self.lpoint += 1
            return "Lpush Success"
        elif l_or_r == 'r':
            self.items[self.rpoint] = num
            self.rpoint -= 1
            return "Rpush Success"
        else:
            return "Please Input 'l' or 'r'"

    def pop(self, l_or_r):
        if l_or_r == 'l':
            if self.lpoint == 0:
                return "Lstack Is Empty"
            else:
                self.lpoint -= 1
                return "L_poped Success"
        elif l_or_r == 'r':
            if self.rpoint == self.maxsize - 1:
                return "Rstack Is Empty"
            else:
                self.rpoint += 1
                return "R_poped Success"
        else:
            return "Please Input 'l' or 'r'"



