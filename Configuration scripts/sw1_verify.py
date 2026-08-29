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
    "port": 5004,
}

verification_commands = [
    "show vlan brief",
    "show interfaces status",
    "show interfaces trunk",
    "show mac address-table",
    "show running-config",
]

connection = None

try:
    connection = ConnectHandler(**switch)

    if switch["secret"]:
        connection.enable()

    for command in verification_commands:
        print(f"\n--- SW1: {command} ---")

        output = connection.send_command(
            command,
            read_timeout=30
        )

        print(output)

    print("\nSW1 verification completed.")

except NetmikoTimeoutException:
    print("SW1 connection timed out.")

except NetmikoAuthenticationException:
    print("SW1 authentication failed.")

except Exception as error:
    print(f"Unexpected error: {error}")

finally:
    if connection is not None:
        connection.disconnect()
