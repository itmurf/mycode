#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
proto.append('dns') # this line will add dns to the end of our list.
protoa.append('dns') # this line will add dns to the end of our list.
print(proto)
proto2 = [ 22, 80, 443, 53 ] #common ports
proto.extend(proto2) 
print(proto)
protoa.append(proto2)
print (protoa)
