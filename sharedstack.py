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
            print "Stack Is Full"
        elif l_or_r == 'l':
            self.items[self.lpoint] = num
            self.lpoint += 1
            print "Lpush Success"
        elif l_or_r == 'r':
            self.items[self.rpoint] = num
            self.rpoint -= 1
            print "Rpush Success"
        else:
            print "Please Input 'l' or 'r'"

    def pop(self, l_or_r):
        if l_or_r == 'l':
            if self.lpoint == 0:
                print "Lstack Is Empty"
            else:
                print "{} Is L_poped".format(self.items[self.lpoint - 1])
                self.lpoint -= 1
        elif l_or_r == 'r':
            if self.rpoint == self.maxsize - 1:
                print "Rstack Is Empty"
            else:
                print "{} Is R_poped".format(self.items[self.rpoint + 1])
                self.rpoint += 1
        else:
            print "Please Input 'l' or 'r'"

if __name__ == "__main__":
    """UT"""
    sharestack = SharedStack(7)
    sharestack.push(1, 'm')
    sharestack.push(1, 'l')
    sharestack.push(2, 'l')
    sharestack.push(3, 'l')
    sharestack.push(4, 'l')
    sharestack.push(5, 'l')
    sharestack.push(1, 'r')
    sharestack.push(2, 'r')
    sharestack.push(3, 'r')
    sharestack.pop('l')
    sharestack.pop('l')
    sharestack.pop('l')
    sharestack.pop('l')
    sharestack.pop('l')
    sharestack.pop('l')
    sharestack.pop('r')
    sharestack.pop('r')
    sharestack.pop('r')
    sharestack.pop('m')
