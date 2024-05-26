# KLA Prealigner Vision Repeatability (Keyence) Control Software

This software provides a graphical user interface (GUI) for controlling the KLA Prealigner Vision Repeatability system using a Keyence device. It enables you to interact with the system through serial and TCP connections, execute macro sequences, and monitor the system's status.

## Features

*   **Serial Communication:** Connect to the NXC100 controller via a serial port and send commands (MTRS, MALN, CSOL, HRST, custom commands).
*   **TCP Communication:** Establish a TCP connection to control the Keyence XG-X system remotely and send trigger commands (Trig 1, Trig 2, PrevCam, NextCam, custom commands).
*   **Macro Execution:** Run predefined macro sequences for automated control of the system.
*   **Logging:** View detailed logs of commands sent and received, system status, and errors.
*   **Status Monitoring:** Monitor the connection status (serial, TCP) and macro execution status in real time.
*   **Alarm Handling:**  Detects and displays alarm messages from the NXC100 controller, including potential causes.

## Usage

1.  **Launch:** Run `main_window.py` to open the GUI.
2.  **Serial Control:**
    *   Select the appropriate COM port from the dropdown.
    *   Click "Connect" to establish a serial connection.
    *   Use the buttons to send commands or enter custom commands in the text box.
3.  **TCP Control:**
    *   Enter the IP address and port of the target device.
    *   Click "Connect" to establish a TCP connection.
    *   Use the buttons to send commands or enter custom commands in the text box.
4.  **Macro Control:**
    *   Set the desired number of alignments.
    *   Click "Start" to begin the macro sequence.
    *   Click "Stop" to interrupt the sequence.

## Configuration (Future Implementation)

*   Serial settings (e.g., baud rate) and TCP settings can be customized in the future.

## Troubleshooting

*   Check the log for error messages.
*   Ensure the correct COM port is selected and the baud rate matches the device settings.
*   Verify the IP address and port are correct for TCP communication.

## Contributing

Contributions are welcome! Feel free to submit issues, bug reports, or feature requests.

## License

This project is licensed under the [MIT License](LICENSE).
