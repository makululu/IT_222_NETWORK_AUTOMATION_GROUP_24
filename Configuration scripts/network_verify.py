from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

devices = [
    {
        "name": "R1",
        "device_type": "cisco_ios_telnet",
        "host": "192.168.109.128",
        "username": "",
        "password": "",
        "secret": "",
        "port": 5006,
    },
    {
        "name": "R2",
        "device_type": "cisco_ios_telnet",
        "host": "192.168.109.128",
        "username": "",
        "password": "",
        "secret": "",
        "port": 5008,
    },
    {
        "name": "SW1",
        "device_type": "cisco_ios_telnet",
        "host": "192.168.109.128",
        "username": "",
        "password": "",
        "secret": "",
        "port": 5004,
    },
    {
        "name": "SW2",
        "device_type": "cisco_ios_telnet",
        "host": "192.168.109.128",
        "username": "",
        "password": "",
        "secret": "",
        "port": 5010,
    },
]

commands = {
    "R1": [
        "show ip interface brief",
        "show ip ospf neighbor",
        "show ip ospf interface brief",
        "show ip route ospf",
    ],

    "R2": [
        "show ip interface brief",
        "show ip ospf neighbor",
        "show ip ospf interface brief",
        "show ip route ospf",
    ],

    "SW1": [
        "show vlan brief",
        "show interfaces trunk",
        "show interfaces status",
        "show mac address-table",
    ],

    "SW2": [
        "show vlan brief",
        "show interfaces trunk",
        "show interfaces status",
        "show mac address-table",
    ],
}

for device in devices:

    connection = None
    name = device["name"]

    details = {
        key: value
        for key, value in device.items()
        if key != "name"
    }

    try:
        print(f"\n========== {name} ==========")

        connection = ConnectHandler(**details)

        if details["secret"]:
            connection.enable()

        for command in commands[name]:

            print(f"\n--- {name}: {command} ---")

            output = connection.send_command(
                command,
                read_timeout=30
            )

            print(output)

    except NetmikoTimeoutException:
        print(f"{name}: Connection timed out.")

    except NetmikoAuthenticationException:
        print(f"{name}: Authentication failed.")

    except Exception as error:
        print(
            f"{name}: Unexpected error: {error}"
        )

    finally:
        if connection is not None:
            connection.disconnect()

print("\nIntegrated network verification completed.")
