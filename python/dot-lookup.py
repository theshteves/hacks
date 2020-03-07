#!/usr/bin/env python3
'''
Object w/ unnecessarily dotted names

Written by Steven Kneiser
'''

class DottedName(object):
    def __getattr__(self, attr):
        self.__dict__[attr] = DottedName()
        return self.__dict__[attr]

if __name__ == '__main__':
    longest = DottedName()
    longest.name.ever.was = 'Steven'
    print(longest.name.ever.was)
