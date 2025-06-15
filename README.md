
# Delay-Tolerant Networking (DTN) Simulator

This project simulates Delay-Tolerant Networking (DTN), a type of network designed to operate effectively over extreme distances such as those encountered in space communications or in environments with intermittent connectivity.

## Author 
**Umma Jarin Toba**

## Project Files

- `dtn_simulator.py` — The main Python script containing the logic for nodes, data transmission, and forwarding.
- `README.md` — This documentation file explaining the project and instructions to run it.

## How to Run

1. Make sure Python 3.6+ is installed on your computer.
2. Open a terminal or command prompt.
3. Run the following command:

   ```bash
   python dtn_simulator.py
   ```

4. You will see console output showing how data is sent and forwarded among the nodes over simulation ticks.

## Overview

- Each `Node` represents a device or station in the network.
- Nodes connect to each other using the `connect()` method.
- Data is sent using `send_data()`. If the destination node is not directly connected, the data is stored temporarily.
- The data is forwarded through intermediate nodes during simulation ticks.
- The simulation is run by `simulate_ticks()`, which processes forwarding over time steps.

## Usage

This code can be extended to real-world applications by implementing actual network communication protocols. You could also build graphical or web interfaces to visualize or control the network.

## Contact

If you have any questions or feedback about the project, feel free to reach out.
