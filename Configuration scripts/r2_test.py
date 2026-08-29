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

testing_commands = [
    "ping 10.24.24.1",
    "ping 172.28.51.10",
    "ping 172.28.81.10",
    "traceroute 172.28.51.10",
]

connection = None

try:
    connection = ConnectHandler(**router)

    if router["secret"]:
        connection.enable()

    for command in testing_commands:
        print(f"\n--- R2 TEST: {command} ---")

        output = connection.send_command(
            command,
            read_timeout=30
        )

        print(output)

    print("\nR2 network testing completed.")

except NetmikoTimeoutException:
    print("R2 connection timed out.")

except NetmikoAuthenticationException:
    print("R2 authentication failed.")

except Exception as error:
    print(f"Unexpected error: {error}")

finally:
    if connection is not None:
        connection.disconnect()
