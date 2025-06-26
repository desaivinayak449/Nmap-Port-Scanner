import nmap

def scan_target(ip, port_range='1-65535'):
	scanner = nmap.PortScanner()
	print(f"[+] Scanning {ip} for ports {port_range}...")
	
	scanner.scan(ip,port_range)
	
	for host in scanner.all_hosts():
		print(f"\nHost: {host} ({scanner[host].hostname()})")
		print(f"State: {scanner[host].state()}")

		for protocol in scanner[host].all_protocols():
			print(f"Protocol: {protocol}")
			ports =  scanner[host][protocol].keys()
			for port in sorted(ports):
                		state = scanner[host][protocol][port]['state']
                		name = scanner[host][protocol][port].get('name', 'unknown')
                		product = scanner[host][protocol][port].get('product', 'unknown')
                		print(f"  Port: {port}\tState: {state}\tService: {name} ({product})")

target_ip= input("Enter Target IP Address:  ")
scan_target(target_ip)
