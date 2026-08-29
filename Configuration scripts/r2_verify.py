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

verification_commands = [
    "show ip interface brief",
    "show ip ospf neighbor",
    "show ip ospf interface brief",
    "show ip route",
    "show ip protocols",
    "show running-config",
]

connection = None

try:
    connection = ConnectHandler(**router)

    if router["secret"]:
        connection.enable()

    for command in verification_commands:
        print(f"\n--- R2: {command} ---")

        output = connection.send_command(
            command,
            read_timeout=30
        )

        print(output)

    print("\nR2 verification completed.")

except NetmikoTimeoutException:
    print("R2 connection timed out.")

except NetmikoAuthenticationException:
    print("R2 authentication failed.")

except Exception as error:
    print(f"Unexpected error: {error}")

finally:
    if connection is not None:
        connection.disconnect()
