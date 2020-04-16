port_list = {
    25:"smtp",
    80:"http",
    443:"https",
    23:"telnet"
}

os = [
    "windows 10",
    "debian",
    "ubuntu",
    "redhat"
]

for individual_os, port in zip(os, port_list):
    print(f"Scanned port {port} on {individual_os} OS for {port_list[port]}")