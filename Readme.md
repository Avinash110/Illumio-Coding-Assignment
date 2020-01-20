The Assignment is to build a firewall like setup which based on the rules accepts a packet if satisfies any 1 of the rule else we will assume the packet is blocked.

To run the above code run the test.py file.

The first approach that I thought of was building up a decision tree. Like if we are given the 2 rules:
	1 - inbound,tcp,80,192.168.1.2
	2 - outbound,tcp,10000-20000,192.168.10.11
we can build something like
	
                    direction
					/        \ 
			inbound/	      \outbound
				  /	           \
			protocol          protocol
			   /				\
		   tcp/					 \tcp
		     / 					  \
		   			.
		   			.
		   			.
and so on and if we reach the leaf node then the packet satisfies atleast one of the rules.
In this system we will typically reduce the number of rules to check by half at direction and protocol level but for port and ip we will have to check for all possible port and ip at that level.
So if we the rules aren't optimally defined we can many nodes for comparison.

The second approach and the approach that I implemented is similar to elastic search. 
For every value in the column let's say inbound for direction, we store the value as key and have list of row number which is unique row identifier in which that value appears.
So if "inbound" is in 2nd and 3rd row, we'll have a map that stores and "tcp" is in 1st and 4rd row
{"inbound": [2,3], "tcp": [1,4]} 

To check if the packet (inbound, tcp) is valid, we'll take the intersection of the 2 lists and if that is an empty that means the packet does not satisfy any rule else there is atleast one rule in which is satisfied by packet.

For port I have initialzed empty set for all the available ports 1-65535, so if 1st row has port 80 there will be a entry of 1 in port 80 set and if 2nd row has range 100-200 for ports from 100 to 200 will have entry of row 2.

For IP address, I have a separate map because I have to match packet's ip adress to every ip address in the csv. I will have to research in order to optimize it.

I have tested both inclusive and exclusive and the test cases are available in test.py file.

Regarding the team preference:
	
	1 - Data Team: Data team because I have 2 years experience in the capacity of Data Engineer, I have worked on entire data pipeline from collecting data to data visualization. More of the details can be found on my resume or you could also check my LinkedIn profile: https://linkedin.com/in/avinashbhojwani11

	2 - Platform Team: I have experience in building framework in NodeJS on top of Express framework which handled routing of requests, request authorization, oauth authentication, caching module. I have also worked building API's in NodeJS which executed queries on database and returned the data to client for rendering data visualization components.