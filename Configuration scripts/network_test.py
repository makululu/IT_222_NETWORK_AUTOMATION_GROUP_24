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

tests = {
    "R1": [
        (
            "R1 -> R2",
            "ping 10.24.24.2"
        ),

        (
            "R1 -> Site B Ticketing Gateway",
            "ping 172.29.51.1"
        ),

        (
            "R1 -> Site B Operations Gateway",
            "ping 172.29.81.1"
        ),
    ],

    "R2": [
        (
            "R2 -> R1",
            "ping 10.24.24.1"
        ),

        (
            "R2 -> Site A Ticketing Gateway",
            "ping 172.28.51.1"
        ),

        (
            "R2 -> Site A Operations Gateway",
            "ping 172.28.81.1"
        ),
    ],

    "SW1": [
        (
            "SW1 VLANs",
            "show vlan brief"
        ),

        (
            "SW1 trunk",
            "show interfaces trunk"
        ),
    ],

    "SW2": [
        (
            "SW2 VLANs",
            "show vlan brief"
        ),

        (
            "SW2 trunk",
            "show interfaces trunk"
        ),
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

        for purpose, command in tests[name]:

            print(f"\n--- {purpose} ---")
            print(command)

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

print("\nIntegrated network testing completed.")

print(
    "End-device tests are performed from VPCS "
    "using Usage_Examples/pc_commands.txt."
)
