from Firewall import Firewall

fw = Firewall("fw.csv")

test_cases_inclusive = [
	#testing exact match
	["inbound", "tcp", 80, "192.168.1.2"],
	#testing ip range lower bound
	["inbound", "udp", 53, "192.168.1.1"],
	#testing ip range upper bound
	["inbound", "udp", 53, "192.168.2.5"],
	#testing ip range in between
	["inbound", "udp", 53, "192.168.2.1"],
	#testing ip range in between overlapping intervals
	["inbound", "udp", 53, "192.168.2.6"],
	#testing port range lower bound
	["outbound", "tcp", 10000, "192.168.10.11"],
	#testing port range upper bound
	["outbound", "tcp", 20000, "192.168.10.11"],
	#testing port range in between
	["outbound", "tcp", 10234, "192.168.10.11"],
	#testing port range in between overlapping intervals
	["outbound", "tcp", 20001, "192.168.10.11"],
	#testing upper bound of ip and port
	["outbound","udp",65535,"255.255.255.255"],
	#testing lower bound of ip and port
	["outbound","udp",1,"0.0.0.0"]
]

test_cases_exclusive = [
	#testing port mismatch
	["inbound", "tcp", 81, "192.168.1.2"],
	#testing direction mismatch
	["outbound","udp",53, "192.168.1.5"],
	#testing invalid direction
	["abcd","udp",53, "192.168.1.5"],
	#testing ip mismatch
	["inbound", "tcp", 80, "192.169.1.2"],
	#testing invalid protocol
	["outbound","abcd",10, "192.168.1"],
	#testing port out of lower bound
	["outbound","tcp",0, "192.168.1"],
	#testing port out of upper bound
	["outbound","tcp",655356, "192.168.1"],
	#testing invalid ip
	["outbound","tcp",100, "-192.168.1"],
	#testing invalid ip
	["inbound", "tcp", 80, "-192.169.1.2"]
]

print("Inclusive")
for i,t in enumerate(test_cases_inclusive):
	print("Test Case : ",i + 1," - ",fw.accept_packet(t[0], t[1], t[2], t[3]))

print("Exclusive")
for i,t in enumerate(test_cases_exclusive):
	print("Test Case : ",i + 1," - ",fw.accept_packet(t[0], t[1], t[2], t[3]))