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

testing_commands = [
    "show vlan brief",
    "show interfaces trunk",
    "show mac address-table",
    "show interfaces status",
]

connection = None

try:
    connection = ConnectHandler(**switch)

    if switch["secret"]:
        connection.enable()

    for command in testing_commands:
        print(f"\n--- SW2 TEST: {command} ---")

        output = connection.send_command(
            command,
            read_timeout=30
        )

        print(output)

    print("\nSW2 switching tests completed.")

except NetmikoTimeoutException:
    print("SW2 connection timed out.")

except NetmikoAuthenticationException:
    print("SW2 authentication failed.")

except Exception as error:
    print(f"Unexpected error: {error}")

finally:
    if connection is not None:
        connection.disconnect()
