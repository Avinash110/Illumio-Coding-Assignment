import csv
class Firewall():
	def __init__(self, filePath):
		self.indexedMap = {}
		self.ipaddressMap = {}
		self.portRange = [1,65535]

		self.initPorts()
		self.processCSV(filePath)

	def initPorts(self):
		for i in range(self.portRange[0], self.portRange[1] + 1):
			self.indexedMap[i] = []

	def processCSV(self, filePath):
		with open(filePath, newline='') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',')
			for i, row in enumerate(spamreader):
				if (i > 0):
					direction,protocol,port,ip = row
					if direction not in self.indexedMap:
						self.indexedMap[direction] = []
					if protocol not in self.indexedMap:
						self.indexedMap[protocol] = []
					if ip not in self.ipaddressMap:
						self.ipaddressMap[ip] = []

					self.indexedMap[direction].append(i)
					self.indexedMap[protocol].append(i)
					self.ipaddressMap[ip].append(i)
					self.handlePort(port, i)

	def handlePort(self, port, row):
		if "-" in port:
			startRange, endRange = port.split("-")
			startRange = int(startRange)
			endRange = int(endRange)
			for i in range(startRange, endRange + 1):
				self.indexedMap[i].append(row)
		else:
			port = int(port)
			if port >=1 and port <= 65535:
				self.indexedMap[port].append(row)

	def accept_packet(self, direction, protocol, port, ip):
		if direction not in self.indexedMap:
			return False
		if protocol not in self.indexedMap:
			return False
		if port < 1 or port > 655355:
			return False

		directionRows = set(self.indexedMap[direction])
		protocolRows = set(self.indexedMap[protocol])
		portRows = set(self.indexedMap[port])
		ipRows = set(self.getIPRows(ip))
		return len(list(directionRows & protocolRows & portRows & ipRows)) > 0

	def getIPRows(self, ip):
		ipRows = []
		ipadresses = self.ipaddressMap.keys()
		for ipadress in ipadresses:
			if "-" in ipadress:
				if self.isIpInRange(ipadress, ip):
					ipRows.extend(list(self.ipaddressMap[ipadress]))

			else:
				if(ipadress == ip):
					ipRows.extend(list(self.ipaddressMap[ipadress]))

		return ipRows

	def isIpInRange(self, ipRange, ip):
		startRange, endRange = ipRange.split("-")
		startRange = startRange.split(".")
		endRange = endRange.split(".")
		ip = ip.split(".")
		for i in range(4):
			if ip[i] < startRange[i] or ip[i] > endRange[i]:
				return False
		return True