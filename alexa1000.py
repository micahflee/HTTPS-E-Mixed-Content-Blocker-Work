#!/usr/bin/env python

import sys, os

if __name__ == '__main__':
    # load top 1000 domains
    top1000 = []
    for domain in open('data/top_1000_domains.txt', 'r').readlines():
        if domain.strip() != '':
            top1000.append(domain.strip())
    top1000.sort()

    # load httpse domains
    httpse_domains = []
    for domain in open('data/mcb_domains.txt', 'r').readlines():
        if domain.strip() != '':
            domain = '.'.join(domain.split('.')[-2:])
            if domain not in httpse_domains:
                httpse_domains.append(domain.strip())
    httpse_domains.sort()

    # what's in common?
    common_domains = []
    for alexa_domain in top1000:
        if alexa_domain in httpse_domains:
            print alexa_domain
            

