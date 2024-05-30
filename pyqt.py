from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QLineEdit, QComboBox, QGridLayout, QFrame, QApplication
)
from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from datetime import datetime
import sys


class Dispatcher(QObject):
    connectSerialPort = pyqtSignal(str)
    closeSerialPort = pyqtSignal(str)
    moveToReadyStation = pyqtSignal()
    alignWafer = pyqtSignal()
    chuckHold = pyqtSignal()
    chuckRelease = pyqtSignal()
    sendCustomSerial = pyqtSignal(str)
    quitApplication = pyqtSignal()
    emergencyStop = pyqtSignal()
    connectTCP = pyqtSignal(str, str)
    disconnectTCP = pyqtSignal()
    triggerOne = pyqtSignal()
    triggerTwo = pyqtSignal()
    prevCamera = pyqtSignal()
    nextCamera = pyqtSignal()
    sendCustomTCP = pyqtSignal(str)
    stopSequence = pyqtSignal()
    clearLogDisplay = pyqtSignal()
    initializeSequence = pyqtSignal(str)
    updateTotalCycles = pyqtSignal(str)
    total_cycles_update = pyqtSignal(str)
    updateSerialConnectionStatus = pyqtSignal(bool)
    updateTCPConnectionStatus = pyqtSignal(bool)
    startSequence = pyqtSignal()
    stopSequence = pyqtSignal()
    updateMacroRunningStatus = pyqtSignal(bool)


class SerialControlFrame(QWidget):
    def __init__(self, dispatcher, available_ports=None):
        super().__init__()
        self.dispatcher = dispatcher
        self.serial_connected = False

        layout = QGridLayout()

        self.lbl_com_port = QLabel("COM Port")
        layout.addWidget(self.lbl_com_port, 0, 0)

        self.cbx_com_port = QComboBox()
        self.cbx_com_port.addItems(available_ports if available_ports else [])
        layout.addWidget(self.cbx_com_port, 1, 0)

        self.lbl_baudrate = QLabel("Baud Rate")
        layout.addWidget(self.lbl_baudrate, 0, 1)

        self.lbl_9600 = QLabel("9600")
        layout.addWidget(self.lbl_9600, 1, 1)

        self.btn_connect_serial = QPushButton("Connect")
        self.btn_connect_serial.clicked.connect(lambda: dispatcher.connectSerialPort.emit(self.cbx_com_port.currentText()))
        layout.addWidget(self.btn_connect_serial, 2, 0)

        self.btn_disconnect_serial = QPushButton("Close")
        self.btn_disconnect_serial.clicked.connect(lambda: dispatcher.closeSerialPort.emit(self.cbx_com_port.currentText()))
        layout.addWidget(self.btn_disconnect_serial, 2, 1)

        self.serial_separator0 = QFrame()
        self.serial_separator0.setFrameShape(QFrame.HLine)
        layout.addWidget(self.serial_separator0, 3, 0, 1, 2)

        self.btn_mtrs = QPushButton("MTRS")
        self.btn_mtrs.setEnabled(False)
        self.btn_mtrs.clicked.connect(lambda: dispatcher.moveToReadyStation.emit())
        layout.addWidget(self.btn_mtrs, 4, 0)

        self.btn_maln = QPushButton("MALN")
        self.btn_maln.setEnabled(False)
        self.btn_maln.clicked.connect(lambda: dispatcher.alignWafer.emit())
        layout.addWidget(self.btn_maln, 4, 1)

        self.btn_chuck_on = QPushButton("ChkON")
        self.btn_chuck_on.setEnabled(False)
        self.btn_chuck_on.clicked.connect(lambda: dispatcher.chuckHold.emit())
        layout.addWidget(self.btn_chuck_on, 5, 0)

        self.btn_chuck_off = QPushButton("ChkOFF")
        self.btn_chuck_off.setEnabled(False)
        self.btn_chuck_off.clicked.connect(lambda: dispatcher.chuckRelease.emit())
        layout.addWidget(self.btn_chuck_off, 5, 1)

        self.serial_separator1 = QFrame()
        self.serial_separator1.setFrameShape(QFrame.HLine)
        layout.addWidget(self.serial_separator1, 6, 0, 1, 2)

        self.ent_custom_serial = QLineEdit()
        self.ent_custom_serial.setEnabled(False)
        layout.addWidget(self.ent_custom_serial, 7, 0, 1, 2)

        self.btn_custom_serial_send = QPushButton("Send")
        self.btn_custom_serial_send.setEnabled(False)
        self.btn_custom_serial_send.clicked.connect(lambda: dispatcher.sendCustomSerial.emit(self.ent_custom_serial.text()))
        layout.addWidget(self.btn_custom_serial_send, 8, 0)

        self.btn_quit_application = QPushButton("Quit")
        self.btn_quit_application.clicked.connect(lambda: dispatcher.quitApplication.emit())
        layout.addWidget(self.btn_quit_application, 8, 1)

        self.serial_separator2 = QFrame()
        self.serial_separator2.setFrameShape(QFrame.HLine)
        layout.addWidget(self.serial_separator2, 9, 0, 1, 2)

        self.btn_e_stop = QPushButton("EMERGENCY STOP")
        self.btn_e_stop.clicked.connect(lambda: dispatcher.emergencyStop.emit())
        layout.addWidget(self.btn_e_stop, 10, 0, 1, 2)

        self.setLayout(layout)
        dispatcher.updateSerialConnectionStatus.connect(self.update_serial_connection_status)

    def update_serial_connection_status(self, status):
        print("debug this function from SerialControlFrame")
        self.serial_connected = status
        self.update_button_states()

    def update_button_states(self):
        print("debug this function from SerialControlFrame")
        widgets = [
            self.btn_mtrs,
            self.btn_maln,
            self.btn_chuck_on,
            self.btn_chuck_off,
            self.btn_custom_serial_send,
            self.ent_custom_serial
        ]

        state = True if self.serial_connected else False
        for widget in widgets:
            widget.setEnabled(state)
        self.btn_connect_serial.setEnabled(not state)
        self.btn_disconnect_serial.setEnabled(state)


class TCPControlFrame(QWidget):
    def __init__(self, dispatcher):
        super().__init__()
        self.dispatcher = dispatcher
        self.tcp_connected = False

        layout = QGridLayout()

        self.lbl_ip_address = QLabel("IP Address")
        layout.addWidget(self.lbl_ip_address, 0, 0)

        self.lbl_ip_port = QLabel("IP Port")
        layout.addWidget(self.lbl_ip_port, 0, 1)

        self.txt_ip_address_default = "127.0.0.1"
        self.ent_ip_address = QLineEdit(self.txt_ip_address_default)
        layout.addWidget(self.ent_ip_address, 1, 0)

        self.txt_ip_port_default = "8500"
        self.ent_ip_port = QLineEdit(self.txt_ip_port_default)
        layout.addWidget(self.ent_ip_port, 1, 1)

        self.btn_connect_socket = QPushButton("Connect")
        self.btn_connect_socket.clicked.connect(lambda: dispatcher.connectTCP.emit(self.ent_ip_address.text(), self.ent_ip_port.text()))
        layout.addWidget(self.btn_connect_socket, 2, 0)

        self.btn_disconnect_socket = QPushButton("Close")
        self.btn_disconnect_socket.clicked.connect(lambda: dispatcher.disconnectTCP.emit())
        layout.addWidget(self.btn_disconnect_socket, 2, 1)

        self.tcp_separator0 = QFrame()
        self.tcp_separator0.setFrameShape(QFrame.HLine)
        layout.addWidget(self.tcp_separator0, 3, 0, 1, 2)

        self.btn_t1 = QPushButton("Trig 1")
        self.btn_t1.setEnabled(False)
        self.btn_t1.clicked.connect(lambda: dispatcher.triggerOne.emit())
        layout.addWidget(self.btn_t1, 4, 0)

        self.btn_t2 = QPushButton("Trig 2")
        self.btn_t2.setEnabled(False)
        self.btn_t2.clicked.connect(lambda: dispatcher.triggerTwo.emit())
        layout.addWidget(self.btn_t2, 4, 1)

        self.btn_prev_camera = QPushButton("PrevCam")
        self.btn_prev_camera.setEnabled(False)
        self.btn_prev_camera.clicked.connect(lambda: dispatcher.prevCamera.emit())
        layout.addWidget(self.btn_prev_camera, 5, 0)

        self.btn_next_camera = QPushButton("NextCam")
        self.btn_next_camera.setEnabled(False)
        self.btn_next_camera.clicked.connect(lambda: dispatcher.nextCamera.emit())
        layout.addWidget(self.btn_next_camera, 5, 1)

        self.tcp_separator1 = QFrame()
        self.tcp_separator1.setFrameShape(QFrame.HLine)
        layout.addWidget(self.tcp_separator1, 6, 0, 1, 2)

        self.ent_custom_tcp = QLineEdit()
        self.ent_custom_tcp.setEnabled(False)
        layout.addWidget(self.ent_custom_tcp, 7, 0, 1, 2)

        self.btn_custom_tcp_send = QPushButton("Send")
        self.btn_custom_tcp_send.setEnabled(False)
        self.btn_custom_tcp_send.clicked.connect(lambda: dispatcher.sendCustomTCP.emit(self.ent_custom_tcp.text()))
        layout.addWidget(self.btn_custom_tcp_send, 8, 0)

        self.btn_quit_application = QPushButton("Quit")
        self.btn_quit_application.clicked.connect(lambda: dispatcher.quitApplication.emit())
        layout.addWidget(self.btn_quit_application, 8, 1)

        self.tcp_separator2 = QFrame()
        self.tcp_separator2.setFrameShape(QFrame.HLine)
        layout.addWidget(self.tcp_separator2, 9, 0, 1, 2)

        self.btn_e_stop = QPushButton("EMERGENCY STOP")
        self.btn_e_stop.clicked.connect(lambda: dispatcher.emergencyStop.emit())
        layout.addWidget(self.btn_e_stop, 10, 0, 1, 2)

        self.setLayout(layout)
        dispatcher.updateTCPConnectionStatus.connect(self.update_tcp_connection_status)

    def update_tcp_connection_status(self, status):
        print("debug this function from TCPControlFrame")
        self.tcp_connected = status
        self.update_button_states()

    def update_button_states(self):
        print("debug this function from TCPControlFrame")
        widgets = [
            self.btn_t1,
            self.btn_t2,
            self.btn_prev_camera,
            self.btn_next_camera,
            self.btn_custom_tcp_send,
            self.ent_custom_tcp
        ]

        state = True if self.tcp_connected else False
        for widget in widgets:
            widget.setEnabled(state)
        self.btn_connect_socket.setEnabled(not state)
        self.btn_disconnect_socket.setEnabled(state)


class MacroControlFrame(QWidget):
    def __init__(self, dispatcher, completed_cycles_value=None):
        super().__init__()
        self.total_cycles = "105"

        self.stop_time = None
        self.dispatcher = dispatcher
        self.completed_cycles_value = completed_cycles_value or 0
        self.start_time = None
        self.elapsed_time = "00:00:00"
        self.macro_running = False

        self.serial_connected = False
        self.tcp_connected = True

        layout = QGridLayout()

        self.lbl_alignments = QLabel("Alignments")
        layout.addWidget(self.lbl_alignments, 1, 0)

        self.ent_total_cycles = QLineEdit(self.total_cycles)
        layout.addWidget(self.ent_total_cycles, 2, 0)
        self.ent_total_cycles.editingFinished.connect(self.on_total_cycles_change)

        self.lbl_completed_cycles = QLabel("Completed")
        layout.addWidget(self.lbl_completed_cycles, 1, 1)

        self.ent_completed_cycles = QLineEdit(str(self.completed_cycles_value))
        layout.addWidget(self.ent_completed_cycles, 2, 1)

        self.macro_separator0 = QFrame()
        self.macro_separator0.setFrameShape(QFrame.HLine)
        layout.addWidget(self.macro_separator0, 3, 0, 1, 2)

        self.btn_start = QPushButton("Start")
        self.btn_start.setEnabled(False)
        self.btn_start.clicked.connect(self.starting_sequence)
        layout.addWidget(self.btn_start, 4, 0)

        self.btn_stop = QPushButton("Stop")
        self.btn_stop.clicked.connect(lambda: dispatcher.stopSequence.emit())
        layout.addWidget(self.btn_stop, 4, 1)

        self.btn_clear_log_display = QPushButton("Clear")
        self.btn_clear_log_display.clicked.connect(lambda: dispatcher.clearLogDisplay.emit())
        layout.addWidget(self.btn_clear_log_display, 5, 0)

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setEnabled(False)
        self.btn_reset.clicked.connect(self.reset_sequence)
        layout.addWidget(self.btn_reset, 5, 1)

        self.macro_separator1 = QFrame()
        self.macro_separator1.setFrameShape(QFrame.HLine)
        layout.addWidget(self.macro_separator1, 6, 0, 1, 2)

        self.lbl_start_time = QLabel("Started:")
        layout.addWidget(self.lbl_start_time, 7, 0)

        self.val_start_time = QLabel("00:00:00")
        layout.addWidget(self.val_start_time, 7, 1)

        self.lbl_elapsed_time = QLabel("Elapsed:")
        layout.addWidget(self.lbl_elapsed_time, 8, 0)

        self.val_elapsed_time = QLabel("--:--:--")
        layout.addWidget(self.val_elapsed_time, 8, 1)

        self.lbl_stop_time = QLabel("Stopped:")
        layout.addWidget(self.lbl_stop_time, 9, 0)

        self.val_stop_time = QLabel("--:--:--")
        layout.addWidget(self.val_stop_time, 9, 1)

        self.macro_separator2 = QFrame()
        self.macro_separator2.setFrameShape(QFrame.HLine)
        layout.addWidget(self.macro_separator2, 10, 0, 1, 2)

        self.btn_e_stop = QPushButton("EMERGENCY STOP")
        self.btn_e_stop.clicked.connect(lambda: dispatcher.emergencyStop.emit())
        layout.addWidget(self.btn_e_stop, 11, 0, 1, 2)

        self.setLayout(layout)

        dispatcher.updateSerialConnectionStatus.connect(self.update_serial_connection_status)
        dispatcher.updateTCPConnectionStatus.connect(self.update_tcp_connection_status)
        dispatcher.startSequence.connect(self.set_start_time)
        dispatcher.stopSequence.connect(self.set_stop_time)

        self.update_button_states()

    def on_total_cycles_change(self):
        new_total = self.ent_total_cycles.text()
        self.dispatcher.updateTotalCycles.emit(new_total)
        self.dispatcher.total_cycles_update.emit(new_total)

    def starting_sequence(self):
        self.set_start_time()
        self.dispatcher.initializeSequence.emit(self.ent_total_cycles.text())
        self.macro_running = True
        self.update_elapsed_time()
        self.update_button_states()

    def update_serial_connection_status(self, status):
        print("debug this function from MacroControlFrame")
        self.serial_connected = status
        self.update_button_states()

    def update_tcp_connection_status(self, status):
        print("debug this function from MacroControlFrame")
        self.tcp_connected = status
        self.update_button_states()

    def update_button_states(self):
        self.btn_start.setEnabled(self.serial_connected)
        self.btn_reset.setEnabled(not self.macro_running)

    def set_start_time(self):
        print("debug this function from MacroControlFrame")
        self.start_time = datetime.now()
        self.val_start_time.setText(self.start_time.strftime("%H:%M:%S"))
        print(f"Start time set to: {self.start_time.strftime('%H:%M:%S')}")

    def set_stop_time(self):
        print("debug this function from MacroControlFrame")
        self.stop_time = datetime.now()
        self.val_stop_time.setText(self.stop_time.strftime("%H:%M:%S"))
        print(f"Stop time set to: {self.stop_time.strftime('%H:%M:%S')}")
        self.macro_running = False
        self.update_elapsed_time()
        self.update_button_states()

    def update_elapsed_time(self):
        if self.start_time and self.macro_running:
            elapsed = datetime.now() - self.start_time
            self.elapsed_time = str(elapsed).split('.')[0]  # Format as HH:MM:SS
            self.val_elapsed_time.setText(self.elapsed_time)
            QTimer.singleShot(1000, self.update_elapsed_time)  # Schedule to update every second
        elif self.start_time and self.stop_time:
            elapsed = self.stop_time - self.start_time
            self.elapsed_time = str(elapsed).split('.')[0]  # Format as HH:MM:SS
            self.val_elapsed_time.setText(self.elapsed_time)
        else:
            self.val_elapsed_time.setText("--:--:--")

    def reset_sequence(self):
        print("debug this function from MacroControlFrame")
        print("Sequence Reset")
        self.macro_running = False
        self.start_time = None
        self.stop_time = None
        self.val_start_time.setText("00:00:00")
        self.val_stop_time.setText("--:--:--")
        self.val_elapsed_time.setText("--:--:--")
        self.ent_total_cycles.setText("105")
        self.ent_completed_cycles.setText("0")
        self.update_button_states()


class StatusFrame(QWidget):
    def __init__(self, dispatcher):
        super().__init__()
        self.dispatcher = dispatcher
        self.status_label_width = 16

        layout = QVBoxLayout()

        self.lbl_serial_status = QLabel("Serial: Disconnected")
        self.lbl_serial_status.setFixedWidth(self.status_label_width)
        self.lbl_serial_status.setStyleSheet("color: darkgrey")
        layout.addWidget(self.lbl_serial_status)

        self.lbl_tcp_status = QLabel("TCP: Disconnected")
        self.lbl_tcp_status.setFixedWidth(self.status_label_width)
        self.lbl_tcp_status.setStyleSheet("color: darkgrey")
        layout.addWidget(self.lbl_tcp_status)

        self.lbl_macro_status = QLabel("Macro: Stopped")
        self.lbl_macro_status.setFixedWidth(self.status_label_width)
        self.lbl_macro_status.setStyleSheet("color: darkgrey")
        layout.addWidget(self.lbl_macro_status)

        self.setLayout(layout)
        dispatcher.updateSerialConnectionStatus.connect(self.update_serial_status)
        dispatcher.updateTCPConnectionStatus.connect(self.update_tcp_status)
        dispatcher.updateMacroRunningStatus.connect(self.update_macro_status)

    def update_serial_status(self, status):
        if status:
            self.lbl_serial_status.setText("Serial: Connected")
            self.lbl_serial_status.setStyleSheet("color: white; background-color: green")
        else:
            self.lbl_serial_status.setText("Serial: Closed")
            self.lbl_serial_status.setStyleSheet("color: white; background-color: red")

    def update_tcp_status(self, status):
        if status:
            self.lbl_tcp_status.setText("TCP: Connected")
            self.lbl_tcp_status.setStyleSheet("color: white; background-color: green")
        else:
            self.lbl_tcp_status.setText("TCP: Closed")
            self.lbl_tcp_status.setStyleSheet("color: white; background-color: red")

    def update_macro_status(self, status):
        if status:
            self.lbl_macro_status.setText("Macro: Running")
            self.lbl_macro_status.setStyleSheet("color: white; background-color: green")
        else:
            self.lbl_macro_status.setText("Macro: Stopped")
            self.lbl_macro_status.setStyleSheet("color: white; background-color: red")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.dispatcher = Dispatcher()

        layout = QVBoxLayout()

        self.serial_frame = SerialControlFrame(self.dispatcher, available_ports=["COM1", "COM2", "COM3"])
        layout.addWidget(self.serial_frame)

        self.tcp_frame = TCPControlFrame(self.dispatcher)
        layout.addWidget(self.tcp_frame)

        self.macro_frame = MacroControlFrame(self.dispatcher)
        layout.addWidget(self.macro_frame)

        self.status_frame = StatusFrame(self.dispatcher)
        layout.addWidget(self.status_frame)

        self.setLayout(layout)
        self.setWindowTitle("Control Frame")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
