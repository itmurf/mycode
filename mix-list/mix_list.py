#!/usr/bin/env python3

#Create my_list with IP, port, and state
my_list = [ "192.168.0.5", 5060, "UP" ]

#Display IP
print("The first item in the list (IP): " + my_list[0] )

#Display port
print("The second item in the list (port): " + str(my_list[1]) )

#Display state
print("The last item in the list (state): " + my_list[2] )

#Create new list with ports, IPs, and application.
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#Display statement using different elements of new_list.
print("When I " + new_list[5] + " into IP addresses " + new_list[3] + " or " + new_list[4] + " I am unable to ping ports " + str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2]) )

