from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

switch = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.109.128",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5010,
}

commands = [
    "hostname SW2",

    # VLAN 51 - Ticketing
    "vlan 51",
    "name Ticketing",
    "exit",

    # VLAN 81 - Operations
    "vlan 81",
    "name Operations",
    "exit",

    # SW2 -> R2 trunk
    "interface GigabitEthernet0/1",
    "switchport mode trunk",
    "switchport trunk allowed vlan 51,81",
    "no shutdown",
    "exit",

    # SW2 -> Ticketing-PC2
    "interface GigabitEthernet0/2",
    "switchport mode access",
    "switchport access vlan 51",
    "no shutdown",
    "exit",

    # SW2 -> Operations-PC2
    "interface GigabitEthernet0/3",
    "switchport mode access",
    "switchport access vlan 81",
    "no shutdown",
    "exit",
]

connection = None

try:
    connection = ConnectHandler(**switch)

    if switch["secret"]:
        connection.enable()

    output = connection.send_config_set(commands)
    print(output)

    connection.save_config()

    print("\nSW2 configuration completed successfully.")

except NetmikoTimeoutException:
    print(
        "SW2 connection timed out. "
        "Check GNS3 VM IP, TELNET port, and switch state."
    )

except NetmikoAuthenticationException:
    print(
        "SW2 authentication failed. "
        "Check username, password, and enable password."
    )

except Exception as error:
    print(f"Unexpected error: {error}")

finally:
    if connection is not None:
        connection.disconnect()
