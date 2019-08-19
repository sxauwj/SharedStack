# -*- coding:utf-8 -*-

import unittest
from sharedstack import SharedStack


class TestSharedStack(unittest.TestCase):

    def setUp(self):
        self.sharedstack = SharedStack(3)

    def test_push_and_pop(self):
        # push
        not_l_or_r__push_msg = self.sharedstack.push(1, 'm')

        l_push_msg_1 = self.sharedstack.push(1, 'l')
        l_push_msg_2 = self.sharedstack.push(2, 'l')

        r_push_msg_1 = self.sharedstack.push(1, 'r')
        full_stack_msg = self.sharedstack.push(2, 'r')

        # pop
        not_l_or_r__pop_msg = self.sharedstack.pop('m')

        l_pop_msg_1 = self.sharedstack.pop('l')
        l_pop_msg_2 = self.sharedstack.pop('l')
        l_empty_stack_pop_msg = self.sharedstack.pop('l')

        r_pop_msg_1 = self.sharedstack.pop('r')
        r_empty_stack_pop_msg = self.sharedstack.pop('r')

        self.assertEqual(not_l_or_r__push_msg, "Please Input 'l' or 'r'")

        self.assertEqual(l_push_msg_1, "Lpush Success")
        self.assertEqual(l_push_msg_2, "Lpush Success")
        self.assertEqual(r_push_msg_1, "Rpush Success")
        self.assertEqual(full_stack_msg, "Stack Is Full")

        self.assertEqual(not_l_or_r__pop_msg, "Please Input 'l' or 'r'")

        self.assertEqual(l_pop_msg_1, "L_poped Success")
        self.assertEqual(l_pop_msg_2, "L_poped Success")
        self.assertEqual(l_empty_stack_pop_msg, "Lstack Is Empty")

        self.assertEqual(r_pop_msg_1, "R_poped Success")
        self.assertEqual(r_empty_stack_pop_msg, "Rstack Is Empty")


if __name__ == '__main':
    unittest.main()
