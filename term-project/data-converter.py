#!/usr/bin/python

a = open('poker-hand-testing.data', 'r')

for b in a.readlines():
    print len(b.split(','))

a.close()
