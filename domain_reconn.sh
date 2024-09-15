#!/bin/bash

echo "Enter the target domain: "
read domain

echo "DNS Records:"
dig $domain ANY

echo "NS Records:"
dig $domain NS

echo "MX Records:"
dig $domain MX

echo "SOA Records:"
dig $domain SOA

echo "IP Address:"
nslookup $domain
