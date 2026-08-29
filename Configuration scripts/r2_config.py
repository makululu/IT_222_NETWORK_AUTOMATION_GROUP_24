from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

router = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.109.128",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5008,
}

commands = [
    "hostname R2",

    # R2 -> SW2 trunk
    "interface GigabitEthernet0/0",
    "no shutdown",

    # VLAN 51 - Ticketing
    "interface GigabitEthernet0/0.51",
    "encapsulation dot1Q 51",
    "ip address 172.29.51.1 255.255.255.0",

    # VLAN 81 - Operations
    "interface GigabitEthernet0/0.81",
    "encapsulation dot1Q 81",
    "ip address 172.29.81.1 255.255.255.0",

    # R2 -> R1 backbone
    "interface GigabitEthernet0/1",
    "ip address 10.24.24.2 255.255.255.252",
    "no shutdown",

    # OSPF
    "router ospf 1",
    "router-id 2.2.2.2",
    "network 10.24.24.0 0.0.0.3 area 0",
    "network 172.29.51.0 0.0.0.255 area 0",
    "network 172.29.81.0 0.0.0.255 area 0",
]

connection = None

try:
    connection = ConnectHandler(**router)

    if router["secret"]:
        connection.enable()

    output = connection.send_config_set(commands)
    print(output)

    connection.save_config()

    print("\nR2 configuration completed successfully.")

except NetmikoTimeoutException:
    print(
        "R2 connection timed out. "
        "Check GNS3 VM IP, TELNET port, and R2 state."
    )

except NetmikoAuthenticationException:
    print(
        "R2 authentication failed. "
        "Check username, password, and enable password."
    )

except Exception as error:
    print(f"Unexpected error: {error}")

finally:
    if connection is not None:
        connection.disconnect()
