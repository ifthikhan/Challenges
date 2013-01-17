#!/usr/bin/env python

"""
Count the number of prime numbers below a given number. This uses the
sieve of eratosthenes algorithm (http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
"""

import sys


def prime_numbers_count(max_number):
    prime_list = [True] * max_number
    prime_list[0] = prime_list[1] = False
    primes = []
    for stride, isPrime in enumerate(prime_list):
        if isPrime:
            primes.append(stride)
            for i in xrange(stride, max_number, stride):
                prime_list[i] = False
    return primes


if __name__ == '__main__':
    number = int(sys.argv[1])
    result = prime_numbers_count(number)
    print "The number of primes below %s is %s" % (number, len(result))
    #print "The primes are: %s" % result
