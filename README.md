# UDP Communication and DNS-like Resolver Project

## Overview
This project involves implementing and analyzing UDP communication between a client and a server using Python. The project is divided into two main parts:

### Part A: UDP Communication Analysis

#### Create Client and Server using UDP:
- Implement simple client-server code using the UDP protocol.
- Modify the client to send the **names of the submitters** instead of "hello world".
- Capture and analyze the traffic using **Wireshark**.
- Explain the code and the traffic in Wireshark with textual explanations and screenshots.

#### Explain the Traffic:
- Describe how the code affects the traffic at different layers and fields.
- Focus on the different layers of information in the traffic and the data within them.

### Part B: Digital 144 Service Implementation

#### Implement a UDP Server:
- The server loads a `zone.txt` file containing domain-to-IP mappings.
- Listens for domain queries and responds with the appropriate IP address based on the `zone.txt` file.
- Handles different types of records (A and NS) and responds accordingly.

#### Implement a Resolver Server:
- Forwards queries to a parent server if it doesn't have the answer cached.
- Caches responses for a specified duration and uses the cache to respond to subsequent queries.
- Implements logic to handle chains of NS records and eventually resolve to an A record or a non-existent domain.

#### Implement a Client:
- Sends domain queries to the resolver server and prints the IP address response.
- Runs in a loop, accepting domain inputs from the console.

---

## Requirements

### Programming Language:
- Python 3

### Libraries:
- Only standard Python libraries are allowed.

### Tools:
- **Wireshark** for traffic analysis

---

## Instructions

### 1. Run the Provided Code
- Implement and execute the client-server code.
- Capture traffic and analyze it using **Wireshark**.

### 2. Implement the Server
- Handle domain queries and manage responses based on `zone.txt`.
- Implement required behaviors like timeout and response formatting.

### 3. Implement the Resolver
- Forward queries to the parent server when needed.
- Cache responses and handle chains of NS records effectively.

### 4. Implement the Client
- Send queries and print responses.
- Handle inputs correctly and operate in a loop.

### 5. Analyze Traffic
- Use **Wireshark** to capture and explain the traffic for different scenarios.

### 6. Document Everything
- Create a detailed report with explanations and screenshots.

---

## Notes
- Ensure the server and client run on separate machines or virtual machines.
- Focus on understanding UDP communication, domain resolution, and caching mechanisms.
- Pay attention to the behavior of different code versions and how changes affect traffic.
- Demonstrate proper handling of different record types and caching functionality.

---

## Deliverables
1. **Code**: Fully implemented UDP client, server, and resolver.
2. **Wireshark Captures**: Screenshots and `.pcap` files for analysis.
3. **Report**: Detailed documentation with:
   - Explanations of traffic analysis.
   - Insights into UDP behavior and resolver functionality.
   - Screenshots and descriptions for each scenario.
4. **README.md**: This file to guide reviewers through the project.
