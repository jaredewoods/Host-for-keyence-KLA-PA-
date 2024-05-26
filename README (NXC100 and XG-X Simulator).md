# NXC100 and Keyence XG-X Simulator

This simulator provides a virtual environment for testing and debugging software that interacts with the NXC100 controller via serial communication and the Keyence XG-X vision system via TCP/IP. It emulates both devices, allowing you to develop and test your control software without needing physical hardware.

## Features

*   **NXC100 Serial Emulation:** Simulates the NXC100 controller's serial communication to receive commands and send responses.
*   **Keyence XG-X TCP/IP Emulation:** Simulates the Keyence XG-X vision system's TCP/IP interface to handle trigger commands and send responses.
*   **Configurable Delays:**  Control the delay times for simulated responses from both devices.
*   **Custom Commands:** Send custom serial commands to the NXC100 emulator to test error handling or specific scenarios.
*   **Logging:** View detailed logs of sent and received commands, errors, and other events for both serial and TCP/IP communication.
*   **Automated Responses:** Configurable automatic responses for MTRS and MALN commands from the NXC100 emulator.

## Usage

1.  **Launch:** Run `NXC100_simulator.py` to start the simulator.
2.  **Serial Port:** Select the virtual serial port from the dropdown and click "Connect" to establish communication with the NXC100 emulator.
3.  **TCP Server:** The Keyence XG-X emulator automatically starts a TCP server on 127.0.0.1:8500 to receive trigger commands.
4.  **Controls:** Use the buttons and spinboxes to send commands to the NXC100 emulator, adjust response delays, and toggle automatic responses.
5.  **Log:** Monitor the log area for incoming and outgoing commands, responses, and other events from both the NXC100 and Keyence XG-X emulators.

## Configuration

*   **MTRS Delay:** Adjust the delay (in seconds) for the MTRS response from the NXC100 emulator.
*   **MALN Delay:** Adjust the delay (in seconds) for the MALN response from the NXC100 emulator.
*   **T1 Delay:** Adjust the delay (in seconds) for the T1 (trigger) response from the Keyence XG-X emulator.
*   **Auto Response:** Enable or disable automatic responses for MTRS and MALN commands from the NXC100 emulator.

## License

This project is licensed under the [MIT License](LICENSE).
