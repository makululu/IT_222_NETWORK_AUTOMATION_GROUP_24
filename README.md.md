IT 222 – Assignment 24: Transport Ticketing Network

                 Student Information


|---------------------------|           |---------------------|
| Student Name              |           | Registration Number |
|MAKULULU SAGUDA MASWEKO    |           | 2024/0467           |
|FABIAN PHILIBERT MADILISHA |           |2024/1777            |
|GLORY WILFRED WILSON       |           |2024/1675            |
|DEODATH EFREM NG'ONG'ONALE |           |2024/0274            |


---

              Project Description

This project implements an automated Cisco IOS configuration,
verification, and testing solution for a two-site Transport Ticketing
Network using Python and Netmiko. The network is simulated in GNS3 and
uses VLAN segmentation, Router-on-a-Stick, and OSPF dynamic routing
between two transport office locations.

The automation scripts configure routers and switches, verify device
status, and perform connectivity testing across the network.

---

             Network Features

- VLAN 51 (Ticketing Department)
- VLAN 81 (Operations Department)
- Router-on-a-Stick Inter-VLAN Routing
- OSPF Process 1 Area 0
- Automated Configuration using Netmiko
- Automated Verification Scripts
- Automated Network Testing Scripts
- Two-Site Enterprise Network Design
- GNS3 Network Simulation

---

             Addressing Plan

| Item | Value |
|------|--------|
| VLAN 51 | Ticketing |
| VLAN 81 | Operations |
| Site A Ticketing | 172.28.51.0/24 |
| Site A Operations | 172.28.81.0/24 |
| Site B Ticketing | 172.29.51.0/24 |
| Site B Operations | 172.29.81.0/24 |
| R1 ↔ R2 Backbone | 10.24.24.0/30 |
| OSPF | Process 1, Area 0 |

---

             Topology

SITE A ↔ R1 ↔ OSPF Backbone ↔ R2 ↔ SITE B

VLAN 51 = Ticketing  
VLAN 81 = Operations

---
              Folder Structure

```text
IT222_Assignment24_Transport_Ticketing_Network/
│
├── Configuration_Scripts/
├── GNS3_Project_File/
├── Templates/
├── Usage_Examples/
├── requirements.txt
├── README.md

  
