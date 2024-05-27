alarm_dict = {
    "0020": {
        "0001": {
            "Message": "CPU COMMUNICATION ERROR",
            "Location of Defect": "NCP30",
            "Signal of Defect": "",
            "Cause": "An error occurred in communications between boards when the control power turned ON due to",
            "Potential Causes": [
                "Insertion of the circuit board is not completed",
                "Defective circuit board",
                "Corrupt memory on the CF "
            ],
            "Sub-Code Description": "The sub code stands for the defective board"
        },
        "0032": {
            "Message": "CPU COMMUNICATION ERROR",
            "Location of Defect": "AXC01",
            "Signal of Defect": "",
            "Cause": "An error occurred in communications between boards when the control power turned ON due to",
            "Potential Causes": [
                "Insertion of the circuit board is not completed",
                "Defective circuit board",
                "Corrupt memory on the CF"
            ],
            "Sub-Code Description": "The sub code stands for the defective board"
        }
    },
    "0021": {
        "0032": {
            "Message": "COMMUNICATION ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "",
            "Cause": "The communications CPU for the AXC01 detected an error when the control power turned ON due to",
            "Potential Causes": [
                "Defective connection of communication cable for servopack",
                "Defective connection of terminal connector",
                "Defective circuit board",
                "Corrupt memory on the CF"
            ],
            "Sub-Code Description": ""
        }
    },
    "0030": {
        "0032": {
            "Message": "ROM ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The system program of AXC01 is damaged",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0060": {
        "0001": {
            "Message": "COMMUNICATION ERROR (I/O MODULE)",
            "Location of Defect": "I/O MODULE",
            "Signal of Defect": "",
            "Cause": "An error was detected in communications with an I/O module board (NIF30) when the control power turned ON",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0100": {
        "0001": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": "",
            "Cause": "An error was detected in communications with the AXC01",
            "Potential Causes": [
                "Abnormal AXC01 serial communication Watch Dog value"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0002": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": "",
            "Cause": "An error was detected in communications with the AXC01",
            "Potential Causes": [
                "AXC01 serial communication watch dog missed one scan cycle"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "0200": {
        "0000:005F": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "",
            "Cause": "The parameter file is damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF"
            ],
            "Sub-Code Description": ""
        }
    },
    "0210": {
        "0000": {
            "Message": "MEMORY ERROR (SYSTEM CONFIGDATA)",
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": "",
            "Cause": "The system configuration information data are damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        }
    },
    "0220": {
        "0001": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": "",
            "Cause": "The management data of job files are damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        },
        "0002": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": "",
            "Cause": "The job files are damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        },
        "0003": {
            "Message": "MEMORY ERROR (JOB MNG DATA)",
            "Location of Defect": "JOB MNG DATA",
            "Signal of Defect": "",
            "Cause": "The management data of position data files are damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        }
    },
    "0230": {
        "0000": {
            "Message": "MEMORY ERROR (LADDER PRG FILE)",
            "Location of Defect": "LADDER PRG FILE",
            "Signal of Defect": "",
            "Cause": "The concurrent I/O ladder program is damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        }
    },
    "0270": {
        "0000": {
            "Message": "MEMORY ERROR (SYSTEM DATA FILE)",
            "Location of Defect": "SYSTEM DATA FILE",
            "Signal of Defect": "",
            "Cause": "The system configuration data is damaged due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        }
    },
    "0300": {
        "0002": {
            "Message": "VERIFY ERROR (SYSTEM CONFIGDATA)",
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": "",
            "Cause": "The setting of concurrent I/O parameter is incorrect due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        },
        "0003": {
            "Message": "VERIFY ERROR (SYSTEM CONFIGDATA)",
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": "",
            "Cause": "An invalid value is set for the segment clock due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        },
        "0004": {
            "Message": "VERIFY ERROR (SYSTEM CONFIGDATA)",
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": "",
            "Cause": "Inconsistency was detected in axis related parameters due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        },
        "0008": {
            "Message": "VERIFY ERROR (SYSTEM CONFIGDATA)",
            "Location of Defect": "SYSTEM CONFIGDATA",
            "Signal of Defect": "",
            "Cause": "The function designation for the concurrent I/O parameter is incorrect due to",
            "Potential Causes": [
                "corrupt memory on the CF",
                "corrupt memory on the NCP30"
            ],
            "Sub-Code Description": ""
        }
    },
    "0310": {
        "0000": {
            "Message": "VERIFY ERROR (CMOS MEMORY SIZE)",
            "Location of Defect": "CMOS MEMORY SIZE",
            "Signal of Defect": "",
            "Cause": "The CMOS memory capacity is different from its initial setting",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0320": {
        "0001": {
            "Message": "VERIFY ERROR (I/O MODULE)",
            "Location of Defect": "I/O MODULE",
            "Signal of Defect": "",
            "Cause": "The function of the connected I/O module is different from the set function",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0330": {
        "0000": {
            "Message": "VERIFY ERROR (SENSOR FUNCTION)",
            "Location of Defect": "SENSOR FUNCTION",
            "Signal of Defect": "",
            "Cause": "Inconsistency was detected in the application setting parameters",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0400": {
        "0032": {
            "Message": "PARAMETER TRANSMISSION ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred during the parameter/ file transfer to the AXC01 due to",
            "Potential Causes": [
                "Defective connection of communication cable for servopack",
                "Defective connection of terminal connector",
                "Defective circuit board",
                "Corrupt memory on the CF"
            ],
            "Sub-Code Description": ""
        }
    },
    "0410": {
        "0032": {
            "Message": "MODE CHANGE ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred during startup sequence processing with the AXC01, and the system did not startup normally",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0500": {
        "0000": {
            "Message": "SEGMENT PROC NOT READY",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "Motion command processing was not completed within the specified time",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0510": {
        "0032": {
            "Message": "SOFTWARE VERSION UNMATCH",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The combination of the main system program and the AXC01 system program are incorrect",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0900": {
        "0000": {
            "Message": "WATCHDOG TIMER ERROR(NCP 30)",
            "Location of Defect": "NCP30",
            "Signal of Defect": "",
            "Cause": "An insertion error of the NCP30 circuit board or defective circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "0950": {
        "0000": {
            "Message": "CPU ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The servo board #1 is defective",
            "Potential Causes": [
                "An error was detected in the CPU of servo board #1"],
            "Sub-Code Description": ""
        }
    },
    "1001": {
        "0001:0018": {
            "Message": "ROM ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error is found at the sum check of the system programs for the AXC01",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "1030": {
        "0000": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "RCD,RCxG parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "0001": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "ROxG parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "0002": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "SVD,SVxG parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "0003": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "SVMxG parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "0004": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "S1CxG,S2C,S3C,S4C parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "0005": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "S1D,S2D,S3D,S4D parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "0006": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "CIO parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "0007": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "FD parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "0008": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "A1P parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "0009": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "RS parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "000A": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "S1E parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "000B": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "SVxB parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "000C": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "AMCxG parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "000D": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "SVPxG parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "000E": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "MFxG parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        },
        "000F": {
            "Message": "MEMORY ERROR (PARAMETER FILE)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "SVxS parameter error",
            "Cause": "This alarm occurs when there is a mismatch between the parameter file data and the CF data",
            "Potential Causes": [
                "Another possibility is corrupt CF data or corrupt memory"
            ],
            "Sub-Code Description": "The sub code stands for the parameter type"
        }
    },
    "1031": {
        "0001:0030": {
            "Message": "MEMORY ERROR (MOTION1)",
            "Location of Defect": "MOTION1",
            "Signal of Defect": "The macro definition file",
            "Cause": "The file data used by MOTION are damaged",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective data"
        }
    },
    "1050": {
        "0001:0002": {
            "Message": "SET:UP PROCESS ERROR (SYSCON)",
            "Location of Defect": "SYSCON",
            "Signal of Defect": "",
            "Cause": "The motion instruction did not start up",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "1051": {
        "0001:000C": {
            "Message": "SET-UP PROCESS ERROR (MOTION)",
            "Location of Defect": "MOTION1",
            "Signal of Defect": "",
            "Cause": "This alarm is caused by an incomplete set up of the MOTION program file",
            "Potential Causes": [],
            "Sub-Code Description": "The subcode shows the software internal process"
        }
    },
    "1100": {
        "0000:FFFF": {
            "Message": "SYSTEM ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An unknown alarm was detected because of noise or control error",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the detected error code"
        }
    },
    "1101": {
        "0000:00FF": {
            "Message": "SYSTEM ERROR (SYSTEM 1)",
            "Location of Defect": "SYSTEM 1",
            "Signal of Defect": "",
            "Cause": "An error occurred during the system control check due to a software bugs or invalid NCP30 RAM data",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "1102": {
        "0000:00FF": {
            "Message": "SYSTEM ERROR (SYSTEM 2)",
            "Location of Defect": "SYSTEM 2",
            "Signal of Defect": "",
            "Cause": "An error occurred during the system control check due to a software bugs or invalid NCP30 RAM data",
            "Potential Causes": [],
            "Sub-Code Description": "The subcode shows the software internal process"
        }
    },
    "1103": {
        "0000:0008": {
            "Message": "SYSTEM ERROR (EVENT)",
            "Location of Defect": "EVENT",
            "Signal of Defect": "",
            "Cause": "An error occurred during the system event data control check due to a software bugs or invalid NCP30 RAM data",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the detected error code"
        }
    },
    "1104": {
        "0080": {
            "Message": "SYSTEM ERROR (CIO)",
            "Location of Defect": "CIO",
            "Signal of Defect": "",
            "Cause": "This alarm is caused by an invalid CIO parameter",
            "Potential Causes": [
                "Other possible causes are a corrupt CF memory or NCP30 memory"
            ],
            "Sub-Code Description": ""
        }
    },
    "1105": {
        "07D0": {
            "Message": "SYSTEM ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "",
            "Cause": "The status setting to base block is different from that of base block signal reading from JL056",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "2710": {
            "Message": "SYSTEM ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "",
            "Cause": "ONEN signal is open",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "0000:8027": {
            "Message": "SYSTEM ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "",
            "Cause": "Servo control board detected corrupt internal data due to software bugs or corrupt RAM",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "1200": {
        "0000": {
            "Message": "HIGH TEMPERATURE",
            "Location of Defect": "CPS PSU",
            "Signal of Defect": "",
            "Cause": "The temperature inside the controller (CPS power supply unit) is too high",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1202": {
        "0000": {
            "Message": "FAULT",
            "Location of Defect": "NCP30",
            "Signal of Defect": "",
            "Cause": "An error occurred in the NCP30 due to",
            "Potential Causes": [
                "Defective board",
                "Incorrect connection",
                "software control error"
            ],
            "Sub-Code Description": ""
        }
    },
    "1204": {
        "0001": {
            "Message": "COMMUNICATION ERROR ( MODULE)",
            "Location of Defect": "MODULE",
            "Signal of Defect": "",
            "Cause": "Communications and power supply error occurred in the NIF30 due to",
            "Potential Causes": [
                "Loose X33 connector",
                "Invalid CIO parameter",
                "Corrupt memory in the NCP30 "
            ],
            "Sub-Code Description": ""
        }
    },
    "1207": {
        "0001:0003": {
            "Message": "BROKEN B_ON RELAY FUSE (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "",
            "Cause": "The brake relay fuse was blown",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1208": {
        "0001:0003": {
            "Message": "BROKEN S_ON RELAY FUSE (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "",
            "Cause": "The servo-ON relay fuse was blown",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1209": {
        "0001:0003": {
            "Message": "EXTERNAL WDT BROKEN (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "",
            "Cause": "This alarm is caused by a failure of the external WDT (watch dog timer) circuit on the NIF30 board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1210": {
        "0001:0003": {
            "Message": "SERIAL COMMUNICATION TOGGLE CHECK ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "",
            "Cause": "This alarm is caused by a failure a serial communication toggle check circuit on the NIF30 board",
            "Potential Causes": [
                "Possible causes are a defective circuit or electrical noise"
            ],
            "Sub-Code Description": ""
        }
    },
    "1211": {
        "0001": {
            "Message": "INPUT COMPARISON ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "PBESP signal",
            "Cause": "The signal does not have a match signal as a result the mutual check of a dual signal",
            "Potential Causes": [
                "This alarm can be caused by an error the user wiring, a damaged NIF30 board or electrical noise"
            ],
            "Sub-Code Description": "The sub code stands for the defective signal"
        },
        "0002": {
            "Message": "INPUT COMPARISON ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "PPESP signal",
            "Cause": "The signal does not have a match signal as a result the mutual check of a dual signal",
            "Potential Causes": [
                "This alarm can be caused by an error the user wiring, a damaged NIF30 board or electrical noise"
            ],
            "Sub-Code Description": "The sub code stands for the defective signal"
        },
        "0004": {
            "Message": "INPUT COMPARISON ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "EXESP signal",
            "Cause": "The signal does not have a match signal as a result the mutual check of a dual signal",
            "Potential Causes": [
                "This alarm can be caused by an error the user wiring, a damaged NIF30 board or electrical noise"
            ],
            "Sub-Code Description": "The sub code stands for the defective signal"
        },
        "0020": {
            "Message": "INPUT COMPARISON ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "SAF_F signal",
            "Cause": "The signal does not have a match signal as a result the mutual check of a dual signal",
            "Potential Causes": [
                "This alarm can be caused by an error the user wiring, a damaged NIF30 board or electrical noise"
            ],
            "Sub-Code Description": "The sub code stands for the defective signal"
        },
        "0080": {
            "Message": "INPUT COMPARISON ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "EXSVON signal",
            "Cause": "The signal does not have a match signal as a result the mutual check of a dual signal",
            "Potential Causes": [
                "This alarm can be caused by an error the user wiring, a damaged NIF30 board or electrical noise"
            ],
            "Sub-Code Description": "The sub code stands for the defective signal"
        },
        "0200": {
            "Message": "INPUT COMPARISON ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "FORCE signal",
            "Cause": "The signal does not have a match signal as a result the mutual check of a dual signal",
            "Potential Causes": [
                "This alarm can be caused by an error the user wiring, a damaged NIF30 board or electrical noise"
            ],
            "Sub-Code Description": "The sub code stands for the defective signal"
        },
        "0400": {
            "Message": "INPUT COMPARISON ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "DSW signal",
            "Cause": "The signal does not have a match signal as a result the mutual check of a dual signal",
            "Potential Causes": [
                "This alarm can be caused by an error the user wiring, a damaged NIF30 board or electrical noise"
            ],
            "Sub-Code Description": "The sub code stands for the defective signal"
        },
        "1000": {
            "Message": "INPUT COMPARISON ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "EXDSW signal",
            "Cause": "The signal does not have a match signal as a result the mutual check of a dual signal",
            "Potential Causes": [
                "This alarm can be caused by an error the user wiring, a damaged NIF30 board or electrical noise"
            ],
            "Sub-Code Description": "The sub code stands for the defective signal"
        },
        "8000": {
            "Message": "INPUT COMPARISON ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "FST signal",
            "Cause": "The signal does not have a match signal as a result the mutual check of a dual signal",
            "Potential Causes": [
                "This alarm can be caused by an error the user wiring, a damaged NIF30 board or electrical noise"
            ],
            "Sub-Code Description": "The sub code stands for the defective signal"
        }
    },
    "1212": {
        "0001:0003": {
            "Message": "PLD MUTUAL MONITOR ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "",
            "Cause": "The input comparison error occurred",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1213": {
        "0001:0003": {
            "Message": "MUTUAL WDT ERROR (NIF30)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "",
            "Cause": "The input comparison error occurred",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1214": {
        "0001:0003": {
            "Message": "PBESP RELAY STICKING",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The emergency stop button of teach pendant PBESP is melted and stuck",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1215": {
        "0001:0003": {
            "Message": "PPESP RELAY STICKING",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The emergency stop button of programming pendant PPESP is melted and stuck",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1216": {
        "0001:0003": {
            "Message": "EXESP RELAY STICKING",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The external emergency stop button EXESP is melted and stuck",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1217": {
        "0001:0003": {
            "Message": "S_ON RELAY STICKING",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The servo-ON relay is melted and stuck",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1218": {
        "0001:0003": {
            "Message": "B_ON RELAY STICKING",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The brake relay is melted and stuck",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1219": {
        "0000": {
            "Message": "ANOTHER PLD EXT WDT ERROR (NIF BOARD)",
            "Location of Defect": "NIF30",
            "Signal of Defect": "",
            "Cause": "The watchdog timer checking the safety circuit is incorrect",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1300": {
        "0000": {
            "Message": "SERVO CPU SYNCHRONIZING ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The connection between the NCP30 and the AXC01 is abnormal",
            "Potential Causes": [
                "The cable between the NCP30 and the AXC01 is incomplete",
                "The connection of the terminal connector is incomplete",
                "The NCP30 is defective",
                "The AXC01 is defective"
            ],
            "Sub-Code Description": ""
        }
    },
    "1301": {
        "0001": {
            "Message": "COMMUNICATION ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "Watch dog error",
            "Cause": "The communication between the NCP30 and the AXC01 is abnormal",
            "Potential Causes": [
                "The cable between the NCP30 and the AXC01 is improper",
                "The connection of the terminal connector is incomplete",
                "The NCP30 defect",
                "The AXC01 defect "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0002": {
            "Message": "COMMUNICATION ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "JL040 alarm",
            "Cause": "The communication between the NCP30 and the AXC01 is abnormal",
            "Potential Causes": [
                "The cable between the NCP30 and the AXC01 is improper",
                "The connection of the terminal connector is incomplete",
                "The NCP30 defect",
                "The AXC01 defect "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0003": {
            "Message": "COMMUNICATION ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "Communication status error",
            "Cause": "The communication between the NCP30 and the AXC01 is abnormal",
            "Potential Causes": [
                "The cable between the NCP30 and the AXC01 is improper",
                "The connection of the terminal connector is incomplete",
                "The NCP30 defect",
                "The AXC01 defect "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "1302": {
        "0001": {
            "Message": "COMMUNICATION ERROR (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "Interruption detected",
            "Cause": "The communication between the AXC01 and the NTU30 is abnormal",
            "Potential Causes": [
                "The AXC01 is abnormal",
                "The NTU30 is abnormal",
                "The cable between the AXC01 and the NTU30 is abnormal"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0002": {
            "Message": "COMMUNICATION ERROR (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "Status error",
            "Cause": "The communication between the AXC01 and the NTU30 is abnormal",
            "Potential Causes": [
                "The AXC01 is abnormal",
                "The NTU30 is abnormal",
                "The cable between the AXC01 and the NTU30 is abnormal"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "006E": {
            "Message": "COMMUNICATION ERROR (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "Communication loop back error",
            "Cause": "The communication between the AXC01 and the NTU30 is abnormal",
            "Potential Causes": [
                "The AXC01 is abnormal",
                "The NTU30 is abnormal",
                "The cable between the AXC01 and the NTU30 is abnormal"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "006F": {
            "Message": "COMMUNICATION ERROR (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "MechatroLink data reception error",
            "Cause": "The communication between the AXC01 and the NTU30 is abnormal",
            "Potential Causes": [
                "The AXC01 is abnormal",
                "The NTU30 is abnormal",
                "The cable between the AXC01 and the NTU30 is abnormal"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "1303": {
        "0000:FFFF": {
            "Message": "ARITHMETIC ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "",
            "Cause": "An error occurred in control arithmetic process or parameter arithmetic process",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1304": {
        "0000": {
            "Message": "EX-AXIS BOARD NOT INSTALLED",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The external board (AXD01) is not mounted although an external axis is specified",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1306": {
        "0001:01FF": {
            "Message": "AMPLIFIER TYPE MISMATCH",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The type of the amplifier displayed in axis data is different from the type in the system configuration",
            "Potential Causes": [
                "The type of the amplifier is not correct",
                "The type of the amplifier is different from the type in the system configuration",
                "Defective amplifier",
                "Defective AXC01 "
            ],
            "Sub-Code Description": "The sub code stands for Physical axis"
        }
    },
    "1307": {
        "0001:01FF": {
            "Message": "ENCODER TYPE MISMATCH",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The type of the encoder displayed in the axis data is different form the type of the encoder set in the system configuration",
            "Potential Causes": [
                "The type of the encoder is not correct",
                "System configuration is not correct",
                "Defective encoder",
                "Defective AXC01",
                "Defective connection of encoder cable"
            ],
            "Sub-Code Description": "The sub code stands for Physical axis"
        }
    },
    "1308": {
        "0001": {
            "Message": "CONVERTER TYPE MISMATCH",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The converter model set in the system configuration is different from that of the one mounted",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1309": {
        "0001": {
            "Message": "HARDWARE ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "",
            "Cause": "Converter hardware is incorrect",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1310": {
        "0001": {
            "Message": "CHARGE ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "",
            "Cause": "The voltage of main DC circuit did not rise above DC40V",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1311": {
        "0001": {
            "Message": "A/D DETECTION ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "",
            "Cause": "Abnormal current data is detected",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1312": {
        "0001": {
            "Message": "ID ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "",
            "Cause": "Converter type mismatch is detected by servo control board during power-up",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1325": {
        "0001:001F": {
            "Message": "COMMUNICATION ERROR (ENCODER)",
            "Location of Defect": "ENCODER",
            "Signal of Defect": "",
            "Cause": "Communication error occurred between the encoder and the AXC01 due to",
            "Potential Causes": [
                "Misconnection of encoder",
                "Noise from external devices",
                "Incorrect motor type",
                "Defective servo control circuit board or encoder "
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "1326": {
        "0001:001F": {
            "Message": "DEFECTIVE ENCODER ABSOLUTE DATA",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The encoder data error is detected at power-up. The encoder data exceeds preset limit value",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "1328": {
        "0001:001F": {
            "Message": "DEFECTIVE SERIAL ENCODER",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "Encoder internal data error is detected in serial communication between the controller and the encoder",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "1329": {
        "0001:001F": {
            "Message": "DEFECTIVE SERIAL ENCODER COMMAND",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "Encoder command execution error is detected in serial communication between the controller and the encoder",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "1330": {
        "0001:001F": {
            "Message": "MICRO PROGRAM TRANSMIT ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "Defective servo control circuit board (Occurred only when the control power supply turned ON.)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "1343": {
        "0065": {
            "Message": "COMMUNICATION ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "Communication status error",
            "Cause": "Serial communication error between the AXC01 and the COBCB030GAA",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0066": {
            "Message": "COMMUNICATION ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "Command timeout",
            "Cause": "Serial communication error between the AXC01 and the COBCB030GAA",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0067": {
            "Message": "COMMUNICATION ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "Transmission error",
            "Cause": "Serial communication error between the AXC01 and the COBCB030GAA",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0068": {
            "Message": "COMMUNICATION ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "Check sum error of received data",
            "Cause": "Serial communication error between the AXC01 and the COBCB030GAA",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0069": {
            "Message": "COMMUNICATION ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "Error code reception",
            "Cause": "Serial communication error between the AXC01 and the COBCB030GAA",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "006A": {
            "Message": "COMMUNICATION ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "Received command error",
            "Cause": "Serial communication error between the AXC01 and the COBCB030GAA",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "1352": {
        "0001:001F": {
            "Message": "SERIAL CORRECTION FAILED",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error was detected in bit shifting compensation",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "1355": {
        "0001:001F": {
            "Message": "SERIAL ENC MULTITURN LIMIT ERR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The NXC100 checks the multiple rotation number of the encoder. This alarm occurs when the parameter of the multiple rotation number is not set to the appropriate value",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "1360": {
        "0000": {
            "Message": "PA NOT INSTALLED",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The prealigner is not mounted although use of the prealigner has been selected",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1500": {
        "0000": {
            "Message": "PLD INTERNAL MUTUAL MONITOR ERROR (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1501": {
        "0000": {
            "Message": "SVMX RELAY STICKING (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1502": {
        "0000": {
            "Message": "TACTOR STICKING (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1503": {
        "0000": {
            "Message": "INPUT COMPARISON ERROR (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1504": {
        "0000": {
            "Message": "TUSON RELAY BREAKDOWN (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1505": {
        "0000": {
            "Message": "B_ON RELAY FUSE BREAKDOWN (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1506": {
        "0000": {
            "Message": "MAIN TACTOR RELAY FUSE BREAKDOWN (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1507": {
        "0000": {
            "Message": "S_ON RELAY FUSE BREAKDOWN (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1508": {
        "0000": {
            "Message": "MUTUAL WDT ERROR (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1509": {
        "0000": {
            "Message": "EXTERNAL WDT OVER (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1510": {
        "0000": {
            "Message": "EXTERNAL WDT BREAKDOWN (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1511": {
        "0000": {
            "Message": "SERIAL COMMUNICATION TOGGLE CHECK ERROR (SERVO I/O)",
            "Location of Defect": "SERVO I/O",
            "Signal of Defect": "",
            "Cause": "PLD internal mutual monitoring error is sent from the TU circuit board",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "1514": {
        "0000": {
            "Message": "OVERHEAT (AMPLIFIER)",
            "Location of Defect": "AMPLIFIER",
            "Signal of Defect": "",
            "Cause": "Amplifier overheated",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4000": {
        "0000:0017": {
            "Message": "MEMORY ERROR (TOOL FILE)",
            "Location of Defect": "TOOLFILE",
            "Signal of Defect": "",
            "Cause": "The memory for the tool file is damaged",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for tool file number"
        }
    },
    "4004": {
        "0000": {
            "Message": "MEMORY ERROR (HOME POS FILE)",
            "Location of Defect": "HOME POS FILE",
            "Signal of Defect": "",
            "Cause": "The memory for the home positioning file is damaged",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4005": {
        "0000": {
            "Message": "MEMORY ERROR (SECOND HOME POS)",
            "Location of Defect": "SECOND HOME POS FILE",
            "Signal of Defect": "",
            "Cause": "The memory for the second home position file is damaged",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4026": {
        "0000:0099": {
            "Message": "MEMORY ERROR(CONDITION FILE)",
            "Location of Defect": "CONDITION FILE",
            "Signal of Defect": "",
            "Cause": "The memory for the condition file is damaged. The sub code is a file number. in which checksum error happened",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4100": {
        "0001": {
            "Message": "OVERRUN (ROBOT AXIS)",
            "Location of Defect": "ROBOT AXIS",
            "Signal of Defect": "",
            "Cause": "NXC100 received robot overrun signal. The signal is disabled at default, so the possible causes are wiring defects or board defects",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4101": {
        "0001": {
            "Message": "OVERRUN (EXTERNAL AXIS)",
            "Location of Defect": "EXTERNAL AXIS",
            "Signal of Defect": "",
            "Cause": "NXC100 received external unit overrun signal. The signal is disabled at default, so the possible causes are wiring defects or board defects",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4102": {
        "0001": {
            "Message": "SYSTEM DATA HAS BEEN CHANGED",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when a servo on command is executed without a power cycle after changing system parameters",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4109": {
        "0000": {
            "Message": "DC24V POWER SUPPLY FAILURE (I/ O)",
            "Location of Defect": "I/O MODULE",
            "Signal of Defect": "",
            "Cause": "This alarm is caused by no 24vdc power at the controller x33 connector",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4110": {
        "0001": {
            "Message": "SHOCK SENSOR ACTIVATION",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "NXC100 received the robot shock sensor signal. The signal is disabled at default, so the possible causes are wiring defects or board defects",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4111": {
        "0000": {
            "Message": "BRAKE FUSE BREAKDOWN",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the brake output relay fuse for NTU30 is broken. The possible causes are NTU30 board defects, or, less often, contact failure or noise",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4119": {
        "0000": {
            "Message": "FAN ERROR (IN CONTROL BOX)",
            "Location of Defect": "IN CONTROL BOX",
            "Signal of Defect": "",
            "Cause": "The rotation speed of in-panel cooling fan decreased",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4200": {
        "0001:0023": {
            "Message": "SYSTEM ERROR (FILE DATA)",
            "Location of Defect": "FILE DATA",
            "Signal of Defect": "",
            "Cause": "The error occurs in the file data access (file edition, CF operation)",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4201": {
        "0001": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Parameter error",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0002": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Access time over",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0003": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Access error",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0004": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Job name error\nInvalid character is used for the job name",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0005": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Existing job open\nThe job name already exists in the memory at the new job creation",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0006": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The area (memory) of the registered job exceeds the available range",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0007": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The job which does not exist in the memory is selected for display",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0008": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The edit-lock job is specified for edition",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0009": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Handle value illegality",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000A": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "System error",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000B": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Sequence number error",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000C": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Step number error",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000D": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The job specified for search does not exist in the memory",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000E": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Invalid command exists in the job.\n(Software unmatch, or data unmatch by software update)",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0010": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Opened handle shortage",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0011": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Write impossibility by multi open",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0012": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The command number exceeds 9999 at the command insertion to the job",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0013": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The step number exceeds 999 at the step insertion to the job",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0014": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "A job was newly created with the same name of the undefined job already specified in the memory",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0063": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Job memory destruction",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [
                "Software bugs or invalid NCP30 RAM memory"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4202": {
        "0001": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Parameter error",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0002": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Access time over",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0003": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Access error",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0004": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Job name error\nInvalid character is used for the job name",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0005": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Existing job open\nThe job name already exists in the memory at the new job creation",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0006": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The area (memory) of the registered job exceeds the available range",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0007": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The job which does not exist in the memory is selected for display",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0008": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The edit-lock job is specified for edition",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0009": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Handle value illegality",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000A": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "System error",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000B": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Sequence number error",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000C": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Step number error",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000D": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The job specified for search does not exist in the memory",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000E": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Invalid command exists in the job.\n(Software unmatch, or data unmatch by software update)",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0010": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Opened handle shortage",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0011": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Write impossibility by multi open",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0012": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The command number exceeds 9999 at the command insertion to the job",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0013": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "The step number exceeds 999 at the step insertion to the job",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0014": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "A job was newly created with the same name of the undefined job already specified in the memory",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0063": {
            "Message": "SYSTEM ERROR (JOB)",
            "Location of Defect": "JOB",
            "Signal of Defect": "Job memory destruction",
            "Cause": "The error occurs in the MOTION job access. (job edition, CF operation)",
            "Potential Causes": [
                "Software bugs or invalid NCP30 RAM memory"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4203": {
        "0001": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Lack of area Uncompleted initialization (Defect)",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0002": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "All axes number are 0. Uncompleted initialization (Defect)",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0003": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Keeping the position on the axes number 0 is unable. Uncompleted initialization (Defect)",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0004": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "The total number of the keeping position is exceeded. Uncompleted initialization (Defect)",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0005": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "The area is exceeds the system setting. Uncompleted initialization (Default)",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0006": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "New acquisition file destruction CMOS memory destruction",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0007": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "The registrable position area (memory) is exceeded",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0008": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Position data destruction CMOS memory destruction",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0009": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Controlling information destruction CMOS memory destruction",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000A": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Illegal position number CMOS memory destruction",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000B": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Unregisterable position data",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000C": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Undefined position",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000D": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Undefined control group",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000E": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Uncompleted initialization",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000F": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "The number of axes for the control groups exceeded the limit",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0010": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "An error occurred in exclusive control",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0011": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "An error occurred in exceptional control",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        }
    },
    "4204": {
        "0001": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Lack of area Uncompleted initialization (Defect)",
            "Cause": "The error occurs in the MOTION position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0002": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "All axes number are 0. Uncompleted initialization (Defect)",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0003": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Keeping the position on the axes number 0 is unable. Uncompleted initialization (Defect)",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0004": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "The total number of the keeping position is exceeded. Uncompleted initialization (Defect)",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0005": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "The area is exceeds the system setting. Uncompleted initialization (Default)",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0006": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "New acquisition file destruction CMOS memory destruction",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0007": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "The registrable position area (memory) is exceeded",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0008": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Position data destruction CMOS memory destruction",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0009": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Controlling information destruction CMOS memory destruction",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000A": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Illegal position number CMOS memory destruction",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000B": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Unregisterable position data",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000C": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Undefined position",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000D": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Undefined control group",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000E": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "Uncompleted initialization",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "000F": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "The number of axes for the control groups exceeded the limit",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0010": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "An error occurred in exclusive control",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        },
        "0011": {
            "Message": "SYSTEM ERROR (POSITION DATA)",
            "Location of Defect": "POSITION DATA",
            "Signal of Defect": "An error occurred in exceptional control",
            "Cause": "The error occurs in the position data access. (During play-back / operating)",
            "Potential Causes": [],
            "Sub-Code Description": "Data stands for the alarm factor"
        }
    },
    "4207": {
        "0001:07D0": {
            "Message": "SYSTEM ERROR (MOTION)",
            "Location of Defect": "MOTION1",
            "Signal of Defect": "",
            "Cause": "A system error (Command-related processing FATAL error) occurred in MOTION due to",
            "Potential Causes": [
                "Software bugs",
                "invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the software internal error code"
        }
    },
    "4208": {
        "0001:002B": {
            "Message": "SYSTEM ERROR (ARITH)",
            "Location of Defect": "ARITH",
            "Signal of Defect": "",
            "Cause": "A system error occurred in the path control section due to",
            "Potential Causes": [
                "Software bugs",
                "invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the software internal error code"
        }
    },
    "4209": {
        "0064:0070": {
            "Message": "OFFLINE SYSTEM ERROR (ARITH)",
            "Location of Defect": "ARITH",
            "Signal of Defect": "",
            "Cause": "A system error occurred in the offline position-data preparation section due to",
            "Potential Causes": [
                "Software bugs",
                "invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the software internal error code"
        }
    },
    "4210": {
        "0001:000B": {
            "Message": "SYSTEM ERROR (Local variable)",
            "Location of Defect": "",
            "Signal of Defect": "Local Variable",
            "Cause": "An error occurred in local variable control process due to",
            "Potential Causes": [
                "Software bugs",
                "invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the software internal error code"
        }
    },
    "4220": {
        "0001": {
            "Message": "SERVO POWER OFF FOR JOB",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The servo power is not supplied to Manipulator",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "0002": {
            "Message": "SERVO POWER OFF FOR JOB",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The servo power is not supplied to Prealigner",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4223": {
        "0002": {
            "Message": "SERVO POWER OFF FOR JOB",
            "Location of Defect": "",
            "Signal of Defect": "ON_EN",
            "Cause": "A safety circuit signal error occurred in I/O unit",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective signal"
        },
        "0003": {
            "Message": "SERVO POWER OFF FOR JOB",
            "Location of Defect": "",
            "Signal of Defect": "OVSPD",
            "Cause": "A safety circuit signal error occurred in I/O unit",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective signal"
        }
    },
    "4301": {
        "0001": {
            "Message": "SAFE CIRCUIT SIGNAL DISAGREEMENT (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "",
            "Cause": "An error occurred in the contactor due to a defective contactor unit (NTU30) circuit board (AXC01)",
            "Potential Causes": [
                "The contactor of contactor unit did not turn ON at servo ON",
                "The signal from the contactor turned OFF while the servo was ON",
                "The signal from the contactor remains ON when the servo turned OFF at emergency stop",
                "The contactor turned ON while the servo was OFF for emergency stop"
            ],
            "Sub-Code Description": "The sub code stands for the defective converter No"
        }
    },
    "4302": {
        "0001": {
            "Message": "CONTACTOR ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The brake relay signal did not turn ON when the servo turned ON",
            "Potential Causes": [
                "The brake relay signal turned OFF while the servo was ON",
                "The brake signal remains ON when the servo turned OFF at emergency stop",
                "The brake signal turned ON while the servo was OFF for emergency stop",
                "Defective NTU30 power-on unit Defective AXC01 circuit board "
            ],
            "Sub-Code Description": "The sub code stands for the defective power-on unit No"
        }
    },
    "4303": {
        "0001": {
            "Message": "BRAKE CIRCUIT ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "No response of charge completion was sent from the converter when the servo turned ON",
            "Potential Causes": [
                "The SERVO READY signal turned OFF while the servo was ON",
                "The SERVO READY signal remains ON when the servo turned OFF at emergency stop",
                "The SERVO READY signal turned ON while the servo was OFF for emergency stop",
                "The primary power supply voltage is too low",
                "The voltage dropped",
                "Defective servo control and/or converter"
            ],
            "Sub-Code Description": "The sub code stands for the defective converter No"
        }
    },
    "4304": {
        "0001": {
            "Message": "CONVERTER INPUT POWER ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "No response of primary power supply input was sent from the converter when the servo turned ON",
            "Potential Causes": [
                "The READY 1 signal remains ON when the servo turned OFF at emergency stop",
                "The READY 1 signal turned ON while the servo was OFF for emergency stop",
                "Incorrect wiring or voltage drop of primary power supply",
                "Defective servo control and/or converter"
            ],
            "Sub-Code Description": "The sub code stands for the defective converter No"
        }
    },
    "4305": {
        "0001": {
            "Message": "CONVERTER CIRCUIT CHARGE ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "No response (READY 2 signal) of charge completion was sent from the converter when the servo turned ON",
            "Potential Causes": [
                "The READY 2 signal turned OFF while the servo was ON",
                "The READY 2 signal remains ON when the servo turned OFF at emergency stop",
                "The READY 2 signal turned ON while the servo was OFF for emergency stop",
                "Incorrect wiring and/or voltage drop of primary power supply",
                "Defective servo control circuit board, converter, and/or amplifier"
            ],
            "Sub-Code Description": "The sub code stands for the defective converter No"
        }
    },
    "4306": {
        "0001:001F": {
            "Message": "AMPLIFIER READY SIGNAL ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "No response \"Power ON\"was sent from the amplifier when the servo turned ON",
            "Potential Causes": [
                "The amplifier READY signal turned OFF while the servo was ON",
                "The amplifier READY signal remains ON when the servo turned OFF at emergency stop",
                "The amplifier READY signal turned ON while the servo was OFF for emergency stop",
                "Defective servo control circuit board, converter, and/or amplifier"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4307": {
        "0001:001F": {
            "Message": "SERVO ON SPEED ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The motion speed of the encoder before the dynamic brake turns OFF in servo ON sequence exceeded the threshold for a certain period",
            "Potential Causes": [
                "The servo power supply turned ON while the manipulator (motor and encoder) was moving"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4308": {
        "0001": {
            "Message": "VOLTAGE DROP (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "",
            "Cause": "The DC power voltage supplied to the SERVOPACK amplifier dropped below 143V due to",
            "Potential Causes": [
                "Low voltage of the primary power supply",
                "Open phase",
                "Defective converter",
                "Defective servo control circuit board "
            ],
            "Sub-Code Description": "The sub code stands for the defective converter No"
        }
    },
    "4311": {
        "0001:001F": {
            "Message": "ENCODER BACK-UP ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "Encoder resetting (initialization) not completed",
            "Potential Causes": [
                "The position data in the encoder was lost due to the voltage drop of encoder backup battery"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4313": {
        "0001:001F": {
            "Message": "SERIAL ENCODER OVER HEAT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The temperature of the encoder exceeded 100 \u00c5~C",
            "Potential Causes": [
                "Encoder thermistor failure "
            ],
            "Sub-Code Description": ""
        }
    },
    "4315": {
        "0001:001F": {
            "Message": "COLLISION DETECT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "Crashed FOUP as FOUP access motion path exceeded given allowable range of position or motion",
            "Potential Causes": [
                "External force Interfering with external devices"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4318": {
        "0001:001F": {
            "Message": "SERIAL ENCODER CORRECT LIMITATION OVER",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The speed feedback value of the serial encoder exceeded the allowable limit",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4320": {
        "0001:001F": {
            "Message": "OVER LOAD (CONTINUE)",
            "Location of Defect": "",
            "Signal of Defect": "CONTINUE",
            "Cause": "The motor torque continuously exceeded the rated torque for a certain period due to",
            "Potential Causes": [
                "The motor tends to be overheated and this brings damages to the motor",
                "Mis-wiring and disconnection of the U, V, W lines of the motor",
                "Improper type of the motor",
                "External force",
                "Interfering with external devices",
                "Defective AXC01 circuit boards",
                "Defective amplifier",
                "Defective motor (Encoder)\n\n\n"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4321": {
        "0001:001F": {
            "Message": "OVER LOAD (INSTANT)",
            "Location of Defect": "",
            "Signal of Defect": "INSTANT",
            "Cause": "The torque a several times as much as the rated torque has been applied to the motor due to",
            "Potential Causes": [
                "The motor tends to be overheated and this brings damages to the motor",
                "Mis-wiring and disconnection of the U, V, W lines of the motor",
                "Improper type of the motor",
                "External force",
                "Interfering with external devices",
                "Defective AXC01 circuit boards",
                "Defective amplifier",
                "Defective motor (Encoder)"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4322": {
        "0001:001F": {
            "Message": "AMPLIFIER OVER LOAD (CONTINUE)",
            "Location of Defect": "",
            "Signal of Defect": "CONTINUE",
            "Cause": "The current a several times as much as the rated current has continuously flown in the amplifier for a certain period due to",
            "Potential Causes": [
                "The motor tends to be overheated and this brings damages to the motor",
                "Mis-wiring and disconnection of the U, V, W lines of the motor",
                "Improper type of the motor",
                "External force",
                "Interfering with external devices",
                "Defective AXC01 circuit boards",
                "Defective amplifier",
                "Defective motor (Encoder)\n"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4323": {
        "0001:001F": {
            "Message": "AMPLIFIER OVER LOAD (INSTANT)",
            "Location of Defect": "",
            "Signal of Defect": "INSTANT",
            "Cause": "The current a several times as much as the rated current has flown in the amplifier for a certain period due to",
            "Potential Causes": [
                "The motor tends to be overheated and this brings damages to the motor",
                "Mis-wiring and disconnection of the U, V, W lines of the motor",
                "Improper type of the motor",
                "External force",
                "Interfering with external devices",
                "Defective AXC01 circuit boards",
                "Defective amplifier",
                "Defective motor (Encoder)\n"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4326": {
        "0001:001F": {
            "Message": "SPEED ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The speed exceeded the limit due to",
            "Potential Causes": [
                "Mis-wiring of the UVW lines of the motor",
                "The motor type is improper",
                "The motor is shifted by the external force",
                "Defective AXC01 circuit boards",
                "Defective motor (Encoder)"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4327": {
        "0001:001F": {
            "Message": "MOTOR ROTATION ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The motor is out of control. This alarm occurs when the motor is operated reversing to the instruction of the correct turning direction",
            "Potential Causes": [
                "Mis-wiring of the UVW lines of the motor",
                "The motor type is improper",
                "The motor is shifted by the external force",
                "Defective AXC01 circuit boards",
                "Defective motor (Encoder)"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4328": {
        "0001:001F": {
            "Message": "SERVO TRACKING ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The axis deviated from the specified position and motion path beyond the allowable range",
            "Potential Causes": [
                "Mis-wiring of the UVW lines of the motor",
                "The motor type is improper",
                "The motor is shifted by the external force",
                "Defective AXC01 circuit boards",
                "Defective motor (Encoder)"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4334": {
        "0001": {
            "Message": "OVER VOLTAGE (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "",
            "Cause": "The DC voltage supplied to the amplifier exceeded 420V due to",
            "Potential Causes": [
                "Overloaded",
                "The primary power supply is too high. (220V+10%)",
                "Converter failure - Defective servo control circuit board"
            ],
            "Sub-Code Description": "The sub code stands for the defective converter No"
        }
    },
    "4335": {
        "0001:001F": {
            "Message": "EARTH FAULT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "Ground fault of the motor power line occurred due to",
            "Potential Causes": [
                "Motor failure",
                "Ground fault of motor line or lead cables",
                "Defective servo control circuit board",
                "Defective SERVOPACK"
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4337": {
        "0001:001F": {
            "Message": "OVER CURRENT (AMPLIFIER)",
            "Location of Defect": "AMPLIFIER",
            "Signal of Defect": "",
            "Cause": "Ground fault of the motor power line occurred due to",
            "Potential Causes": [
                "Motor failure",
                "Ground fault of motor line or lead cables",
                "Defective servo control circuit board",
                "Defective amplifier",
                "Overheating of amplifier "
            ],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4339": {
        "0001": {
            "Message": "INPUT POWER OVER VOLTAGE (CONV)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "",
            "Cause": "The SERVOPACK primary power supply voltage exceeded 242V",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective converter No"
        }
    },
    "4340": {
        "0001": {
            "Message": "TEMPERATURE ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "",
            "Cause": "The temperature of the servo pack (converter) is too high",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective converter No"
        }
    },
    "4353": {
        "0001:001F": {
            "Message": "DEFECTIVE TAUGHT POINT (ENDLESS)",
            "Location of Defect": "ENDLESS",
            "Signal of Defect": "",
            "Cause": "Endless motion impossible The standard position of pre-aligner is not unmatch",
            "Potential Causes": [
                "The feedback pulse value exceeded the maximum value (maximum number of pulses is 536870912)"],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4360": {
        "0001": {
            "Message": "WAFER ALIGNMENT ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "Serial communication timeout",
            "Cause": "An error occurred in communications with the prealigner",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0002": {
            "Message": "WAFER ALIGNMENT ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "Sampling buffer overflow",
            "Cause": "An error occurred in communications with the prealigner",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0003": {
            "Message": "WAFER ALIGNMENT ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "Data number not refreshed",
            "Cause": "An error occurred in communications with the prealigner",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4400": {
        "0001:0006": {
            "Message": "NOT READY (ARITH)",
            "Location of Defect": "ARITH",
            "Signal of Defect": "",
            "Cause": "The arithmetic process for motion control did not complete within regulated time due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4401": {
        "0001:006A": {
            "Message": "SEQUENCE TASK CONTROL ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in job execution process due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4402": {
        "0": {
            "Message": "UNDEFINED COMMAND (ARITH)",
            "Location of Defect": "ARITH",
            "Signal of Defect": "",
            "Cause": "An undefined command was issued to the path control section due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4404": {
        "0001": {
            "Message": "ARITHMETIC ERROR (MOTION)",
            "Location of Defect": "MOTION",
            "Signal of Defect": "MOVL was instructed for the position where the 1st arm was aligned with 2nd arm",
            "Cause": "This alarm occurs when the path calculating process in the calculation section hasn't succeeded normally",
            "Potential Causes": [
                "The teaching position (MIN, IM1, IM2,, IM3, RDY, STA) for the motion command where the alarm has occurred may have an error.  "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0007": {
            "Message": "ARITHMETIC ERROR (MOTION)",
            "Location of Defect": "MOTION",
            "Signal of Defect": "Teaching position \u2248iMIN, IM1, IM2,, IM3, RDY, STA\u2248j was specified out of the motion range",
            "Cause": "This alarm occurs when the path calculating process in the calculation section hasn't succeeded normally",
            "Potential Causes": [
                "The teaching position (MIN, IM1, IM2,, IM3, RDY, STA) for the motion command where the alarm has occurred may have an error.  "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4405": {
        "0001": {
            "Message": "SELECT ERROR (PARAMETER)",
            "Location of Defect": "PARAMETER FILE",
            "Signal of Defect": "Selection error of motion system parameter",
            "Cause": "A parameter error occurred in the path control section",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4406": {
        "0008": {
            "Message": "GROUP AXIS CONTROL ERROR",
            "Location of Defect": "",
            "Signal of Defect": "Occupation control error",
            "Cause": "An internal control error occurred in a coordinated motion",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0009": {
            "Message": "GROUP AXIS CONTROL ERROR",
            "Location of Defect": "",
            "Signal of Defect": "Jog operation occupation control specification error",
            "Cause": "An internal control error occurred in a coordinated motion",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4413": {
        "0000": {
            "Message": "IMPOSSIBLE LINEAR MOTION (S/ L)",
            "Location of Defect": "",
            "Signal of Defect": "S/L",
            "Cause": "This alarm occurs when the form (folded direction) of 1st and 2nd axes at start point and end point are different in the execution of MOVJ instructions",
            "Potential Causes": [
                "The teaching position for the motion command where the alarm has occurred may have an error"
            ],
            "Sub-Code Description": ""
        }
    },
    "4414": {
        "0001:001F": {
            "Message": "EXCESSIVE SEGMENT (LOW SPEED)",
            "Location of Defect": "",
            "Signal of Defect": "LOW SPEED",
            "Cause": "The manipulator motion speed exceeded the limit (LOW level)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4415": {
        "0001:001F": {
            "Message": "EXCESSIVE SEGMENT (HIGH SPEED)",
            "Location of Defect": "",
            "Signal of Defect": "HIGH SPEED",
            "Cause": "The manipulator motion speed exceeded the limit (HIGH level)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4416": {
        "0001:001F": {
            "Message": "PULSE LIMIT (MIN.)",
            "Location of Defect": "",
            "Signal of Defect": "MIN",
            "Cause": "The manipulator exceeded its motion limit (pulse limit) in the negative (-) direction",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4417": {
        "0001:001F": {
            "Message": "PULSE LIMIT (MAX.)",
            "Location of Defect": "",
            "Signal of Defect": "MAX",
            "Cause": "The manipulator exceeded its motion limit (pulse limit) in the positive (+) direction",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4420": {
        "0001:001F": {
            "Message": "SPECIAL SOFTLIMIT (MIN.)",
            "Location of Defect": "",
            "Signal of Defect": "MIN",
            "Cause": "The manipulator exceeded its motion limit (special software limit) in the negative (-) direction",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4421": {
        "0001:001F": {
            "Message": "SPECIAL SOFTLIMIT (MAX.)",
            "Location of Defect": "",
            "Signal of Defect": "MAX",
            "Cause": "The manipulator exceeded its motion limit (special software limit) in the positive (+) direction",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4422": {
        "0001:001F": {
            "Message": "MECHANICAL INTERFERENCE (MIN.)",
            "Location of Defect": "",
            "Signal of Defect": "MIN",
            "Cause": "The manipulator exceeded its minimum- angle motion limit. (Mechanical interference)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4423": {
        "0001:001F": {
            "Message": "MECHANICAL INTERFERENCE (MAX.)",
            "Location of Defect": "",
            "Signal of Defect": "MAX",
            "Cause": "The manipulator exceeded its maximum- angle motion limit. (Mechanical interference)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4426": {
        "0001:001F": {
            "Message": "PULSE MECHANICAL LIMIT (MIN.)",
            "Location of Defect": "",
            "Signal of Defect": "MIN",
            "Cause": "The manipulator exceeded its motion limit (mechanical limit) in the negative (- ) direction",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4427": {
        "0001:001F": {
            "Message": "PULSE MECHANICAL LIMIT (MAX.)",
            "Location of Defect": "",
            "Signal of Defect": "MAX",
            "Cause": "The manipulator exceeded its motion limit (mechanical limit) in the positive (+) direction",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "4428": {
        "0001:0009": {
            "Message": "SEGMENT CONTROL ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in the real-time processing section that controls the arithmetic section due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4429": {
        "0001:0013": {
            "Message": "WRONG SPECIFIED CONTROL GROUP",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in the manipulator information at job execution due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4430": {
        "0001": {
            "Message": "CPU COMMUNICATION ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in the manipulator information at job execution due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4431": {
        "0001:0006": {
            "Message": "JHM ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "Data error occurred in job control process due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4432": {
        "0001:0009": {
            "Message": "INSTRUCTION INTERPRETER ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in instruction interpretation/ execution process due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4433": {
        "0000": {
            "Message": "UNDEFINED GLOBAL VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "byte type",
            "Cause": "The global variable is not defined",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the variable type"
        }
    },
    "4434": {
        "0001": {
            "Message": "UNDEFINED LOCAL VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "integer type",
            "Cause": "The local  variable is not defined",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the variable type"
        }
    },
    "4435": {
        "0002": {
            "Message": "UNDEFINED LOCAL VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "double-precision integer type",
            "Cause": "The local  variable is not defined",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the variable type"
        },
        "0007": {
            "Message": "UNDEFINED LOCAL VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "byte type",
            "Cause": "The local  variable is not defined",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the variable type"
        }
    },
    "4436": {
        "0003": {
            "Message": "UNDEFINED LOCAL VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "real type",
            "Cause": "The local  variable is not defined",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the variable type"
        }
    },
    "4437": {
        "0004": {
            "Message": "UNDEFINED LOCAL VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "character string type",
            "Cause": "The local  variable is not defined",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the variable type"
        }
    },
    "4438": {
        "0005": {
            "Message": "UNDEFINED LOCAL VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "robot-axis position type",
            "Cause": "The local  variable is not defined",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the variable type"
        },
        "0000": {
            "Message": "UNDEFINED JOB",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The job to be executed is not registered in the memory",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4439": {
        "0006": {
            "Message": "UNDEFINED LOCAL VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "base-axis position type",
            "Cause": "The local  variable is not defined",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the variable type"
        },
        "0000": {
            "Message": "UNDEFINED LAVEL",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in label jump execution. The label for jump destination does not exist in the job",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4440": {
        "0007": {
            "Message": "UNDEFINED LOCAL VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "station-axis position type",
            "Cause": "The local  variable is not defined",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the variable type"
        },
        "0000": {
            "Message": "UNDEFINED RETURN JOB",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "Call source job does not exist in the job call stack",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4441": {
        "0000": {
            "Message": "LACK OF LOCAL VARIABLE AREA",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred when memory area for local variable was obtained. Memory area is lacking because too many local variables in the job are used",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4444": {
        "0000": {
            "Message": "UNSUCCESSFUL FINE POSITIONING",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "When PL = 0 or an external servo turned OFF, the number of the servo error pulses did not fall in the limit range that had been set in a parameter, within the specified time",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4445": {
        "0001:00FF": {
            "Message": "DATA PRESET ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "Data error occurred at job pre-reading reinterpretation due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4446": {
        "0001": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the binary (0/1) data type variable exceeded the limit",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "0002": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the signed 1-byte data type variable is less than the minimum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "0004": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the signed 2-byte data type variable is less than the minimum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "0006": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the signed 4-byte data type variable is less than the minimum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "0008": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the real-number 4-byte data type variable is less than the minimum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "8002": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the signed 1-byte data type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "8003": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the unsigned 1-byte data type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "8004": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the signed 2-byte data type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "8005": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the unsigned 2-byte data type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "8006": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the signed 4-byte data type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "8007": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the unsigned 4-byte data type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "8008": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the real-number 4-byte data type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "800C": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the label-name type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "800D": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the job-name type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "800E": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for the character-string type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "800F": {
            "Message": "OVER VARIABLE LIMIT",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The value for comment type variable exceeded the maximum value",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4449": {
        "0000": {
            "Message": "UNMATCHED D POSNVAR DATA ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The storage destination data (pulse/ Cartesian) is different from the storage source data",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4450": {
        "0001:000E": {
            "Message": "FILE NO. ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the interpretation/ execution process detects abnormal internal data due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4452": {
        "0000": {
            "Message": "STACK MORE THAN 8 (JOB CALL)",
            "Location of Defect": "",
            "Signal of Defect": "JOB CALL",
            "Cause": "An attempt was made to add more than eight stacks in the job call stack",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4453": {
        "0000": {
            "Message": "OVER VARIABLE NO",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The variable number (the variable number which an attempt was made to use for subcode) is out of range",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4459": {
        "0000": {
            "Message": "EXCESSIVE INSTRUCTION EQUATION",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in expression operation. The operation is impossible because the expression is too long",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4460": {
        "0000": {
            "Message": "ZERO DIVIDED OCCURRENCE",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in operation instruction. Zero division occurred",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4466": {
        "0000": {
            "Message": "OFFLINE UNDEFINED COMMAND (ARITH)",
            "Location of Defect": "",
            "Signal of Defect": "ARITH",
            "Cause": "An undefined command was issued to the offline position-data preparation section due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": ""
        }
    },
    "4473": {
        "0000": {
            "Message": "ARITHMETIC ALARM RESET ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The alarm occurred in the calculation section could not be reset due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": ""
        }
    },
    "4474": {
        "0001:0002": {
            "Message": "WRONG CONTROL GROUP AXIS",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The CALL/JUMP destination job could not be executed. An attempt was made to call or jump to a job whose control group cannot be controlled",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the related control-group"
        }
    },
    "4475": {
        "0000": {
            "Message": "CANNOT EXECUTE JOB (NO ROBOT)",
            "Location of Defect": "",
            "Signal of Defect": "NO ROBOT",
            "Cause": "An attempt was made to execute a job without robot axis. The robot axis is not designated for the control-group of the job at execution of a work instruction that uses a manipulator",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4496": {
        "0001:000D": {
            "Message": "PARAMETER ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when an abnormal parameter is detected in the arithmetic process",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4498": {
        "0000": {
            "Message": "CANNOT EXECUTE JOB (NO GRP AXIS)",
            "Location of Defect": "",
            "Signal of Defect": "NO GRP AXIS",
            "Cause": "An error occurred in a job without control group. An attempt was made to execute an instruction that could not be executed in a job without control group",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4499": {
        "0000": {
            "Message": "UNDEFINED POSITION VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The position type variable is not registered. An attempt was made to use the position type variable that was not set",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the variable number"
        }
    },
    "4501": {
        "0000": {
            "Message": "OUT OF RANGE (PARALLEL PROCESS)",
            "Location of Defect": "",
            "Signal of Defect": "PARALLEL PROCESS",
            "Cause": "The number of tasks exceeded the limit. An error occurred in the multi-task control process for the independent control function",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the task number"
        }
    },
    "4507": {
        "0000": {
            "Message": "REFP POS ERROR (SEARCH MOTION)",
            "Location of Defect": "",
            "Signal of Defect": "SEARCH MOTION",
            "Cause": "Incorrect teaching point for search detection",
            "Potential Causes": [
                "The search start point and the motion target point are the same, or the distance between the two points is too short"],
            "Sub-Code Description": ""
        }
    },
    "4508": {
        "0000:0010": {
            "Message": "SPECIFIED ERROR (COORDINATE)",
            "Location of Defect": "COORDINATE",
            "Signal of Defect": "master tool coordinate system",
            "Cause": "An invalid coordinate system was specified. The specified coordinate system does not exist",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the coordinate system"
        },
        "0000": {
            "Message": "SPECIFIED ERROR (COORDINATE)",
            "Location of Defect": "COORDINATE",
            "Signal of Defect": "H-LINK type cylindrical coordinate system",
            "Cause": "An invalid coordinate system was specified. The specified coordinate system does not exist",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the coordinate system"
        }
    },
    "4513": {
        "0001:001F": {
            "Message": "EXCESSIVE SEGMENT (SAFETY1)",
            "Location of Defect": "",
            "Signal of Defect": "LOW",
            "Cause": "At the safety speed 1, the manipulator motion speed exceeded the speed limit value (LOW level)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the axis"
        }
    },
    "4514": {
        "0001:001F": {
            "Message": "EXCESSIVE SEGMENT (SAFETY1)",
            "Location of Defect": "",
            "Signal of Defect": "HIGH",
            "Cause": "At the safety speed 1, the manipulator motion speed exceeded the speed limit value (HIGH level)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the axis"
        }
    },
    "4515": {
        "0001:001F": {
            "Message": "EXCESSIVE SEGMENT (SAFETY2)",
            "Location of Defect": "",
            "Signal of Defect": "LOW",
            "Cause": "At the safety speed 2, the manipulator motion speed exceeded the speed limit value (LOW level)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the axis"
        }
    },
    "4516": {
        "0001:001F": {
            "Message": "EXCESSIVE SEGMENT (SAFETY2)",
            "Location of Defect": "",
            "Signal of Defect": "HIGH",
            "Cause": "At the safety speed 2, the manipulator motion speed exceeded the speed limit value (HIGH level)",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the axis"
        }
    },
    "4517": {
        "0000": {
            "Message": "SEARCH MONITOR SET ERROR (SERVO)",
            "Location of Defect": "SERVO",
            "Signal of Defect": "",
            "Cause": "An error occurred in search/monitoring mode settings in servo section due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the related control-group "
        }
    },
    "4518": {
        "0000": {
            "Message": "SEARCH MON RELEASE ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in search/monitoring mode releasing in servo section due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": ""
        }
    },
    "4521": {
        "0000:0001": {
            "Message": "WRONG JOB TYPE",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "A robot job was started from the concurrent job at CALL/JUMP instruction execution",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "0000:1001": {
            "Message": "WRONG JOB TYPE",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "A concurrent job was started from the robot job at CALL/JUMP instruction execution",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "1000:0001": {
            "Message": "WRONG JOB TYPE",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "A system job was started from the robot job at CALL/JUMP instruction execution",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4524": {
        "0000": {
            "Message": "CANNOT EXECUTE INST (CONCUR JOB)",
            "Location of Defect": "",
            "Signal of Defect": "CONCUR JOB",
            "Cause": "There was an un-executable instruction such as move instruction in the concurrent job",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4525": {
        "0000": {
            "Message": "SPECIFIED JOB EXECUTION IMPOSSIBILITY",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred at startup of multi-system job. The specified job could not be executed",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4528": {
        "0000": {
            "Message": "SYNTAX ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in the instruction syntax. The function and the corresponding instruction data is inconsistent in the system software",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the box number"
        }
    },
    "4537": {
        "0001:0003": {
            "Message": "OFFLINEMAIL BOX PROCESSING ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An error occurred in mail box control in the offline processing section due to",
            "Potential Causes": [
                "Software bugs",
                "Invalid NCP30 RAM memory "
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "4543": {
        "0000": {
            "Message": "JOB CALL STACK ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "At job return, an attempt was made to fetch a data from an empty job call stack or to stack a data in the job call stack that is full",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4544": {
        "0001": {
            "Message": "MID$ ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The first character of character string to be extracted is null at MID$ instruction execution",
            "Potential Causes": [],
            "Sub-Code Description": ""
        },
        "0002": {
            "Message": "MID$ ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The extraction start position exceeds the character string length at MID$ instruction execution",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4546": {
        "0000": {
            "Message": "CANNOT EXECUTE SYSTEM JOB",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The system job could not be executed",
            "Potential Causes": [
                "An error in the system number of system job"],
            "Sub-Code Description": "The sub code stands for the system number"
        }
    },
    "4547": {
        "0000": {
            "Message": "PRIMITIVE ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The error occurred in the OS",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the error code from the OS"
        }
    },
    "4548": {
        "0000": {
            "Message": "CANNOT OPERATE SPECIFIED EVENT QUE",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The specified event could not be operated at INIEVNT instruction execution",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4549": {
        "0000": {
            "Message": "INIEVNT NOT EXECUTED",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "INIEVNT instruction was not executed before having executed the event related process",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the system number"
        }
    },
    "4550": {
        "0000": {
            "Message": "CANNOT EXECUTE INST (USER JOB)",
            "Location of Defect": "",
            "Signal of Defect": "USER JOB",
            "Cause": "The specified instruction in the user job could not be executed",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the system number"
        }
    },
    "4599": {
        "0000": {
            "Message": "SERVO COMMAND ERROR",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "An abnormal response was returned from the servo control section. The servo control processing has not completed",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4606": {
        "0000": {
            "Message": "GLOBAL VARIABLE AREA OVERFLOW",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "The memory area of global variable exceeded the limit value. An error occurred in the value of parameter that defines the number of global (user) variables",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4628": {
        "0000": {
            "Message": "DUPLICATE WRITE VARIABLE",
            "Location of Defect": "",
            "Signal of Defect": "",
            "Cause": "In the command which returns multiple outputs, same variable is used for the setting value for outputs",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "4800": {
        "0000": {
            "Message": "WDT ERROR (CONVERTER)",
            "Location of Defect": "CONVERTER",
            "Signal of Defect": "",
            "Cause": "Watchdog timer error in the converter. No response from the converter",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9001": {
        "0000:0004": {
            "Message": "Manipulator / Pre-Aligner Secondary Power OFF [ W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the servos are off and a command is sent that requires the servo power to be on",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9002": {
        "0001": {
            "Message": "Manipulator Homing Not Completed [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if any motion command other than MABS or MRLK, MRLN, ISYS is received when the manipulator is not located in the ISYS position, MIN or, RDY positions",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9003": {
        "0001": {
            "Message": "CRSM Command Un-executable [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "CRSM command was received even though CHLT command hadn't been received",
            "Cause": "This alarm occurs when the CHLT command has not been executed or the external HOLD signal is OPEN when CRSM command is requested from host",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0002": {
            "Message": "CRSM Command Un-executable [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "CRSM command was received while external HOLD signal (EXHOLD) was OPEN",
            "Cause": "This alarm occurs when the CHLT command has not been executed or the external HOLD signal is OPEN when CRSM command is requested from host",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9004": {
        "0001:001B": {
            "Message": "MTRS Command Not Completed [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the manipulator is not located in ready position when MGET or MPUT or MPNT is requested",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected"
        }
    },
    "9005": {
        "0001": {
            "Message": "Execution Disabled Command [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "An un-executable command for the specified unit was sent",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0003": {
            "Message": "Execution Disabled Command [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "CSRV command (Servo ON) for manipulator was received during alarm occurrence",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0004": {
            "Message": "Execution Disabled Command [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "CSRV command (Servo ON) for manipulator was received during emergency stop",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0005": {
            "Message": "Execution Disabled Command [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "CSRV command (Servo ON) for pre-aligner was received in the system of which parameter was set to \"Pre-aligner setting: Disabled\"",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0006": {
            "Message": "Execution Disabled Command [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "CSRV command (Servo ON) for pre-aligner was received during alarm occurrence",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0007": {
            "Message": "Execution Disabled Command [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "CSRV command (Servo ON) for pre-aligner was received during emergency stop",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0009": {
            "Message": "Execution Disabled Command [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "CLFT command was received even though the parameter of the system was set to \"Lifter existence: w/o lifter\"or \"Lifter control enable/disable: Disabled\"",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000C": {
            "Message": "Execution Disabled Command [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "In the system of which Upper End-Effector is not Edge Grip, SPOS and SABS for mapping position were received",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000D": {
            "Message": "Execution Disabled Command [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "ISYS command for pre-aligner was received even though the parameter of the system was set to \"Pre-aligner setting: Disabled\"",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000E": {
            "Message": "Execution Disabled Command [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "SPRM and DPRM were received during Servo ON status",
            "Cause": "This alarm occurs if the requested command cannot be executed by the cause indicated by the sub code",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9006": {
        "0001:000D": {
            "Message": "Disabled Point Motion [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when a point that the manipulator cannot move to is specified by MPNT command",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9007": {
        "0001:0002": {
            "Message": "Execution Disabled for ISYS Command for Pre-Aligner [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if ISYS for the manipulator hasn't been completed when ISYS command is requested by the host of the pre-aligner",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9008": {
        "0001": {
            "Message": "Impossible to Read Mapping Data [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if RMAP command is received for a station at which mapping has not been executed",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9009": {
        "0001": {
            "Message": "Uploading/Downloading [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if another command is received while uploading / downloading position data or parameters",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9010": {
        "0001:0031": {
            "Message": "Position Unregistered [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the teaching for the specified station has not finished when a command is requested from host",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9011": {
        "0001": {
            "Message": "Incorrect Station Attribute [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "Control method of swung wrist axis (Parameter i300 to i319) value of the corresponding station is set to other than 0/1/2",
            "Cause": "This alarm occurs in the following cases",
            "Potential Causes": [
                "Teaching is executed for the station which has an incorrect parameter setting",
                "A via point, which is not defined in the station attribute parameter, is taught"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0002": {
            "Message": "Incorrect Station Attribute [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "Automatic ready position generation (Parameter i320 to i339) of the corresponding station is set to other than 0/1",
            "Cause": "This alarm occurs in the following cases",
            "Potential Causes": [
                "Teaching is executed for the station which has an incorrect parameter setting",
                "A via point, which is not defined in the station attribute parameter, is taught"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0003": {
            "Message": "Incorrect Station Attribute [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "Number of via point (Parameter i340 to i359) value of the corresponding station is set to other than 0/1/2/3",
            "Cause": "This alarm occurs in the following cases",
            "Potential Causes": [
                "Teaching is executed for the station which has an incorrect parameter setting",
                "A via point, which is not defined in the station attribute parameter, is taught"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0004": {
            "Message": "Incorrect Station Attribute [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "End-Effector Swappable position (Parameter i360 to i379) value of the corresponding station is set to 0 - 31",
            "Cause": "This alarm occurs in the following cases",
            "Potential Causes": [
                "Teaching is executed for the station which has an incorrect parameter setting",
                "A via point, which is not defined in the station attribute parameter, is taught"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0005": {
            "Message": "Incorrect Station Attribute [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "The IM3 position, of the station which was defined as \"IM3: None\" in Number of via point (Parameter i340 to i359), was taught",
            "Cause": "This alarm occurs in the following cases",
            "Potential Causes": [
                "Teaching is executed for the station which has an incorrect parameter setting",
                "A via point, which is not defined in the station attribute parameter, is taught"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0006": {
            "Message": "Incorrect Station Attribute [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "The IM2 position, of the station which was defined as \"IM2: None\" in Number of via point (Parameter i340 to i359), was taught",
            "Cause": "This alarm occurs in the following cases",
            "Potential Causes": [
                "Teaching is executed for the station which has an incorrect parameter setting",
                "A via point, which is not defined in the station attribute parameter, is taught"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0007": {
            "Message": "Incorrect Station Attribute [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "The IM1 position, of the station which was defined as \"IM1: None\" in Number of via point (Parameter i340 to i359), was taught",
            "Cause": "This alarm occurs in the following cases",
            "Potential Causes": [
                "Teaching is executed for the station which has an incorrect parameter setting",
                "A via point, which is not defined in the station attribute parameter, is taught"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9031": {
        "0001": {
            "Message": "Unit Number Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the command for the pre-aligner is received in pre-aligner unit disabled system. It also occurs if the command of which unit number is set to other than 1,2 is received",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9032": {
        "0001": {
            "Message": "Undefined Command Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if an undefined command is received. In addition, this alarm occurs in case that a command is requested to a wrong unit",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9033": {
        "0001:00BF": {
            "Message": "Message Parameter Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the parameter attached to a command is not correct when a command is requested from host",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9035": {
        "0001:000B": {
            "Message": "CEMG Command Executed [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the CEMG command is received while the unit is moving, and also after receiving CEMG command, the motion command is received before receiving CCLR command",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9036": {
        "0001:000C": {
            "Message": "Access Permission Error 1 [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "Time-out of access permission signal 1 to the specified station occurs. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The access permission signal 1 is not input",
                "Incorrect wiring between the host and the controller"
            ],
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected"
        }
    },
    "9037": {
        "0001:000C": {
            "Message": "Access Permission Error 2 [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "Time-out of access permission signa2 1 to the specified station occurs. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The access permission signal 1 is not input",
                "Incorrect wiring between the host and the controller"
            ],
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected"
        }
    },
    "9038": {
        "0001:000C": {
            "Message": "Access Permission Error 3 [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "Time-out of access permission signal 3 to the specified station occurs. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The access permission signal 1 is not input",
                "Incorrect wiring between the host and the controller"
            ],
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected"
        }
    },
    "9039": {
        "0001:000C": {
            "Message": "Access Permission Error 4 [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "Time-out of access permission signal 4 to the specified station occurs. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The access permission signal 1 is not input",
                "Incorrect wiring between the host and the controller"
            ],
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected"
        }
    },
    "9040": {
        "0001:000C": {
            "Message": "Access Permission Error 5 [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "Time-out of access permission signal 5 to the specified station occurs. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The access permission signal 1 is not input",
                "Incorrect wiring between the host and the controller"
            ],
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected"
        }
    },
    "9041": {
        "0001:000C": {
            "Message": "Access Permission Error 6 [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "Time-out of access permission signal 6 to the specified station occurs. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The access permission signal 1 is not input",
                "Incorrect wiring between the host and the controller"
            ],
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected"
        }
    },
    "9042": {
        "0001:000C": {
            "Message": "Access Permission Error 7 [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "Time-out of access permission signal 7 to the specified station occurs. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The access permission signal 1 is not input",
                "Incorrect wiring between the host and the controller"
            ],
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected"
        }
    },
    "9043": {
        "0001:000C": {
            "Message": "Access Permission Error 8 [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "Time-out of access permission signal 8 to the specified station occurs. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The access permission signal 1 is not input",
                "Incorrect wiring between the host and the controller"
            ],
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected"
        }
    },
    "9046": {
        "0001": {
            "Message": "Home Motion Disabled [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the manipulator doesn't meet the requirements for the HOME command when MHOM or ISYS from host is executed",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9049": {
        "0001": {
            "Message": "Home Motion Disabled [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the manipulator doesn't meet the requirements for the HOME command when MHOM or ISYS from host is executed",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9050": {
        "0001:0003": {
            "Message": "Access Permission for Pre-Aligner Stage Error 1 [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the command to move the manipulator to the pre-aligner station is executed while the pre-aligner is operating",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9051": {
        "0001": {
            "Message": "Pre-Aligner Station Access Interlock Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the manipulator is instructed to access the pre-aligner while the pre-aligner is chucking a wafer. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The wafer is not released",
                "The parameter setting value is incorrect",
                "The foreign objects are blocking the chucking face",
                "Vacuum air failure",
                "Pressure switch failure\n\n"
            ],
            "Sub-Code Description": ""
        }
    },
    "9052": {
        "0001:0013": {
            "Message": "Wafer Presence Check Time-out [W2]",
            "Location of Defect": "Lower end-effector",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the pressure switch cannot detect a wafer within the time specified in the manipulator parameter I030/i031 (Set value at shipping: 200, Unit: 10ms). ",
            "Potential Causes": [
                "Teaching Error",
                "Error in command sending order",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum Leak",
                "Pressure Switch Failure\n",
                "CDA Leak",
                "Grip sensor failure"
            ],
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs"
        }
    },
    "9053": {
        "0001:0015": {
            "Message": "Wafer Absence Check Time-out [W2]",
            "Location of Defect": "Lower end-effector",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the pressure switch doesn't detect the absence of the wafer within the time specified in the manipulator parameter I030/i031 (Set value at shipping: 200, Unit: 10ms). ",
            "Potential Causes": [
                "Teaching Error",
                "Error in command sending order",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum blockage",
                "Pressure Switch Failure\n"
            ],
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs"
        }
    },
    "9054": {
        "0001:0013": {
            "Message": "Wafer Presence Check Time-out [W2]",
            "Location of Defect": "Upper end-effector",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the pressure switch cannot detect a wafer within the time specified in the manipulator parameter I030/i031 (Set value at shipping: 200, Unit: 10ms). ",
            "Potential Causes": [
                "Teaching Error",
                "Error in command sending order",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum Leak",
                "Pressure Switch Failure\n",
                "CDA Leak",
                "Grip sensor failure"
            ],
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs"
        }
    },
    "9055": {
        "0001:0016": {
            "Message": "Wafer Absence Check Time-out [W2]",
            "Location of Defect": "Upper end-effector",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the pressure switch doesn't detect the absence of the wafer within the time specified in the manipulator parameter I030/i031 (Set value at shipping: 200, Unit: 10ms). ",
            "Potential Causes": [
                "Teaching Error",
                "Error in command sending order",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum blockage",
                "Pressure Switch Failure\n"
            ],
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs"
        }
    },
    "9056": {
        "0001": {
            "Message": "Wafer Drop Error [W2]",
            "Location of Defect": "Lower end-effector",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the pressure switch signal has changed its status from \"with wafer (ON)\" to \"without wafer (OFF)\" while a wafer is being transported. ",
            "Potential Causes": [
                "Teaching Error",
                "Error in command sending order",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum Leak",
                "Pressure Switch Failure\n",
                "CDA Leak",
                "Grip sensor failure"
            ],
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs"
        }
    },
    "9057": {
        "0001": {
            "Message": "Wafer Drop Error [W2]",
            "Location of Defect": "Upper end-effector",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the pressure switch signal has changed its status from \"with wafer (ON)\" to \"without wafer (OFF)\" while a wafer is being transported. ",
            "Potential Causes": [
                "Teaching Error",
                "Parameter setting error",
                "Solenoid Valve Failure",
                "Vacuum Leak",
                "Pressure switch failure\n",
                "CDA Leak",
                "CDA Leak"
            ],
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs"
        }
    },
    "9059": {
        "0001": {
            "Message": "CCD Data Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the data valid for alignment calculation (The pixel position for wafer edge detection  3 to 2047) is less than 75 % out of all sampling data. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The wafer size and the ready position don't correspond with each other",
                "The teaching position for the manipulator is not correct",
                "The standard position of the pre-aligner is not correct",
                "There is dust or dirt or scratch on the lens of the linear sensor or the filter",
                "The wafer is deviated while sampling the data",
                "The linear sensor is broken "
            ],
            "Sub-Code Description": ""
        }
    },
    "9061": {
        "0001": {
            "Message": "Wafer Center Detection Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the center of the wafer cannot be detected. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The wafer is deformed",
                "The dust is attached to the wafer edge",
                "There is dust or dirt or scratches on the lens of the linear sensor or the filter",
                "The wafer has shifted while the data is being sampled",
                "The linear sensor is broken"
            ],
            "Sub-Code Description": ""
        }
    },
    "9062": {
        "0001": {
            "Message": "Excessive Wafer Eccentricity [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the eccentricity of the wafer exceeds 5mm as the result of the alignment. The followings can be the causes for this alarm",
            "Potential Causes": [
                "Teaching error for the manipulator",
                "Incorrect standard position (300mm ready position) of the pre-aligner "
            ],
            "Sub-Code Description": ""
        }
    },
    "9063": {
        "0001": {
            "Message": "Notch/ Orientation Flat Detection Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the notch or the oriental flat cannot be detected. The following cases can be the causes for this alarm",
            "Potential Causes": [
                "The wafer is deformed",
                "Dust is attached to the wafer edge",
                "The wafer is chipped",
                "There is dust or dirt or scratches on the lens of the linear sensor or the filter",
                "The wafer shifted while the data is being sampled",
                "The linear sensor is broken"
            ],
            "Sub-Code Description": ""
        }
    },
    "9065": {
        "0001:0002": {
            "Message": "Mapping Sensor Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the mapping sensor signal is ON (shielded) at the mapping start position. The followings can be the causes for this alarm",
            "Potential Causes": [
                "Teaching error",
                "The sensor is shielded by something",
                "The deviation of the source axis",
                "Mapping sensor error"
            ],
            "Sub-Code Description": ""
        }
    },
    "9067": {
        "0001": {
            "Message": "Mapping Calibration Not Executed [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the number of the wafers detected by MMCA command is not the following number",
            "Potential Causes": [
                "Simple mode (B variable B041=0): 2 wafers",
                "All slot mode (B variable B041=1): Slot number "
            ],
            "Sub-Code Description": ""
        }
    },
    "9068": {
        "0001:0004": {
            "Message": "Mapping Data Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm also occurs if a wafer has been detected at the height where there is no slot by MMAP command",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor, "
        }
    },
    "9070": {
        "0001": {
            "Message": "Non-Host Mode Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if a command is received from the host when the mode is not set to host-mode. ",
            "Potential Causes": [
                "Mode setting mistake",
                "Teaching pendant failure",
                "Teaching pendant dummy connector is broken",
                "NIF30 board failure"
            ],
            "Sub-Code Description": ""
        }
    },
    "9073": {
        "0001:0007": {
            "Message": "Command in Execution Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when another command from the host is received while executing a command",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9076": {
        "0001:0003": {
            "Message": "Message Length Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when receiving a command with a different length specified for each command, or when receiving the command with a message longer than 1024 characters, or when receiving an MACR instruction longer than 64 characters",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9077": {
        "0001": {
            "Message": "Checksum Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the checksum value in the received message differs from the checksum value of the received message. ",
            "Potential Causes": [
                "Message error",
                "Wrong parameter setting",
                "Loosing of a connector",
                "Noise",
                "Communication cable failure",
                "NCP30 board failure "
            ],
            "Sub-Code Description": ""
        }
    },
    "9083": {
        "0001:000F": {
            "Message": "Plunger motion Time-out [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "Lower end-effector",
            "Cause": "This alarm occurs if the sensor flag of the plunger doesn't shade a wafer grip sensor within the time specified by the manipulator parameter I021 (Set value at shipping: 80, Unit 10ms). ",
            "Potential Causes": [
                "The plunger motion speed has decelerated",
                "CDA leak",
                "Solenoid valve failure",
                "Sensor flag has been deformed",
                "Wafer grip sensor failure",
                "Parameter setting error"
            ],
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs"
        }
    },
    "9084": {
        "0001:000F": {
            "Message": "Plunger motion Time-out [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "Upper end-effector",
            "Cause": "This alarm occurs if the sensor flag of the plunger doesn't shade a wafer grip sensor within the time specified by the manipulator parameter I021 (Set value at shipping: 80, Unit 10ms). ",
            "Potential Causes": [
                "The plunger motion speed has decelerated",
                "CDA leak",
                "Solenoid valve failure",
                "Sensor flag has been deformed",
                "Wafer grip sensor failure",
                "Parameter setting error"
            ],
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs"
        }
    },
    "9085": {
        "0001:0006": {
            "Message": "Pre-Aligner Lifter motion Time-out [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the lifter motion is not completed within 2 seconds after the instruction is output toward pre-aligner lifter. ",
            "Potential Causes": [
                "Compressed dry air error",
                "Solenoid valve error",
                "Lifter sensor error",
                "Lifter sensor position deviation"
            ],
            "Sub-Code Description": "The sub code stands for the timing when the alarm occurs"
        }
    },
    "9087": {
        "0001:0004": {
            "Message": "Servo ON Failure [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the servo is not turned ON within 2 seconds after the servo ON instruction is output. This alarm is caused by the other error occurrence",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9088": {
        "0001": {
            "Message": "CCD or Pressure Sensor Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs only when executing the ISYS command of pre-aligner. The pre-aligner moves to 300mm ready position first. And then if the pressure switch detects a wafer and the linear sensor doesn't detect a wafer, the pre-aligner moves to the 200mm ready position. In the case that the linear sensor cannot detect a wafer at 200mm ready position, this alarm occurs. ",
            "Potential Causes": [
                "Compressed dry air error",
                "Wafer deviation",
                "Screening of chucking opening by foreign object",
                "Vacuum piping obstruction",
                "Pressure switch failure"
            ],
            "Sub-Code Description": ""
        }
    },
    "9089": {
        "0001": {
            "Message": "Pre-Aligner Station Access Interlock Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the manipulator with a straight-type end-effector tries to access the pre-aligner when it is not located in the upper end position. The causes for this alarm can be as bellows",
            "Potential Causes": [
                "Operation mistake",
                "Parameter setting error",
                "CDA leak",
                "Lifter sensor position deviation",
                "Lifter sensor failure"
            ],
            "Sub-Code Description": ""
        }
    },
    "9090": {
        "0001": {
            "Message": "Pre-Aligner Station Access Interlock Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when putting a wafer on the pre-aligner even though the linear sensor is detecting a wafer . ",
            "Potential Causes": [
                "Operation mistake",
                "Parameter setting error",
                "CDA leak",
                "Lifter sensor position deviation",
                "Lifter sensor failure"
            ],
            "Sub-Code Description": ""
        }
    },
    "9091": {
        "0001:0002": {
            "Message": "No Pre-Aligner Wafer [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the wafer cannot be chucked with in the time specified in the pre-aligner parameter i030 (set value at shipping: 100, unit: 10ms ) when executing MALN and MACA. ",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Vacuum leak",
                "Pressure switch failure "
            ],
            "Sub-Code Description": ""
        }
    },
    "9092": {
        "0001": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "CCHK command was received during emergency stop",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0002": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "CCLR command was received during emergency stop",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0003": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "CSRV command (Servo ON) for manipulator was received during emergency stop",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0004": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "Emergency stop was requested while servo ON processing for manipulator was being executed",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0005": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "CSRV command (Servo ON) for pre-aligner was received during emergency stop",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0006": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "Emergency stop was requested while servo ON processing for pre-aligner was being executed",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0007": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "CLFT command was received during emergency stop",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0008": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "Emergency stop for the manipulator was received",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0009": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "Emergency stop for the pre-aligner was received",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0010": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "Emergency stop for the pre-aligner was received",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "0011": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "HRST command was received during emergency stop.\n",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000A": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "MACR command was received during emergency stop",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000B": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "MACR command was received during emergency stop",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000C": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "Motion command was received during emergency stop",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000D": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "ISYS command was received during emergency stop",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000E": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "Control command other than CEMG, CCLR, and HRST was received during emergency stop",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        },
        "000F": {
            "Message": "Emergency Stop [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "Emergency stop for the manipulator was received",
            "Cause": "This alarm occurs when",
            "Potential Causes": [
                "There is no wafer on the pre-aligner",
                "Emergency stop button on teaching pendant is pressed",
                "External emergency stop signal is OPEN",
                "A command is requested under the status that the emergency stop on teaching pendant is being pressed",
                "the teaching pendant dummy connector is not connected",
                "external emergency stop signal is OPEN"
            ],
            "Sub-Code Description": "The sub code stands for the alarm factor"
        }
    },
    "9093": {
        "0001:0004": {
            "Message": "Pre-Aligner Lifter Position Error [W2}",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if alignment or calibration is requested when the pre-aligner lifter, of which setting is \"Set pre-aligner lifter\" and \"No pre-aligner lifter control\", is not located in the lower end position",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9094": {
        "0001": {
            "Message": "Pre-Aligner Wafer Chuck Time-out [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the wafer cannot be chucked within the time specified in the pre-aligner parameter i030 (set value at shipping: 100, unit: 10ms) when executing CCHK command. ",
            "Potential Causes": [
                "No wafer is on the pre-aligner",
                "Vacuum leaking",
                "Pressure switch failure "
            ],
            "Sub-Code Description": ""
        }
    },
    "9095": {
        "0001": {
            "Message": "Pre-Aligner Wafer Release Time-out Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the chuck/release operation cannot be executed within the time specified in the pre-aligner parameter I030 (set value at shipping: 100, unit: 10ms) when executing CCHK command. The causes of this alarm are",
            "Potential Causes": [
                "Blockage of vacuum air",
                "Solenoid valve failure",
                "Pressure Switch system failure "
            ],
            "Sub-Code Description": ""
        }
    },
    "9096": {
        "0001": {
            "Message": "CCD or Pressure Sensor Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the linear sensor detects the wafer even though the pressure switch is not detecting any wafer when executing ISYS command. ",
            "Potential Causes": [
                "Blockage of vacuum air",
                "There is dust or dirt or scratches on the lens of the linear sensor or the filter",
                "Linear sensor failure",
                "Vacuum leak",
                "Pressure switch failure "
            ],
            "Sub-Code Description": ""
        }
    },
    "9097": {
        "0001:0007": {
            "Message": "User Task Stopped [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "The alarm also occurs if the user task cannot start up by CCLR or MABS, MRLK, MRLR, ISYS",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the command in which the alarm is detected"
        }
    },
    "9098": {
        "0001:0005": {
            "Message": "System Error [F]",
            "Location of Defect": "F",
            "Signal of Defect": "",
            "Cause": "Failure in error number: detects the error as an undefined error, \"0000\", though the system error signal is on",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9100": {
        "0001": {
            "Message": "MACRO Accept Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "Manipulator",
            "Cause": "A new transfer command is sent during the process of another transfer command",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the unit in which the alarm is detected"
        },
        "0002": {
            "Message": "MACRO Accept Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "Pre-aligner",
            "Cause": "A new transfer command is sent during the process of another transfer command",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the unit in which the alarm is detected"
        }
    },
    "9101": {
        "0001:0023": {
            "Message": "Position Calculation Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if the route calculated during teaching a position or during a system motion command is outside the motion range of the manipulator",
            "Potential Causes": [
                "The following causes are when instructing teaching position",
                "Blockage of vacuum air",
                "Position name is instructed incorrectly. (such as STA)",
                "End-Effector is instructed incorrectly. (1/ 2)",
                "Parameter error R460 to R479 and R480 to R499",
                "The following causes are when moving to relative position",
                "The motion distance instruction is out of the operation range",
                "When executing a transport system command",
                "Parameter error R120 to R319 (Transfer offset)", ],
            "Sub-Code Description": "Sub code differs depending on the command at alarm occurrence"
        }
    },
    "9102": {
        "0001": {
            "Message": "System JOB Not Registered [F]",
            "Location of Defect": "F",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if any system JOB is registered",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9103": {
        "0001": {
            "Message": "System JOB Not Started [F]",
            "Location of Defect": "F",
            "Signal of Defect": "",
            "Cause": "System JOB is stopped because of other alarm occurrences",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9104": {
        "0001:000C": {
            "Message": "SAFE Signal OPEN [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "",
            "Cause": "This alarm occurs in the following cases",
            "Potential Causes": [
                "Fence signal (both SAFF1 and 2 ) is open while the manipulator or prealigner is moving",
                "CCLR, CSRV, MACR, ISYS or motion command is received in the status that fence signal ( both SAFF1 and 2 ) is open", ],
            "Sub-Code Description": "Sub code differs depending on the command at alarm occurrence"
        }
    },
    "9105": {
        "0001:000C": {
            "Message": "EXSVON Signal OPEN [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "",
            "Cause": "This alarm occurs in the following cases",
            "Potential Causes": [
                "External servo power ON signal (EXSVON) is open while the manipulator or pre-aligner is moving",
                "CCLR, CSRV, MACR, ISYS or motion command is received in the status that external servo power ON signal is open", ],
            "Sub-Code Description": "Sub code differs depending on the command at alarm occurrence"
        }
    },
    "9106": {
        "0001:000A": {
            "Message": "EXHOLD Signal OPEN [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs if CCLR, MACR, ISYS or motion command is received in the status that external hold signal (EXHOLD) is open",
            "Potential Causes": [],
            "Sub-Code Description": "Sub code differs depending on the command at alarm occurrence"
        }
    },
    "9107": {
        "0001": {
            "Message": "Controller Battery Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the voltage of the battery for memory backup of the controller becomes lower than 2.8V. In case of the occurrence of this alarm, the alarm code is sent by the completion response for the first command after the alarm occurrence",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    },
    "9108": {
        "0001:001F": {
            "Message": "Serial Encoder Battery Error [W2]",
            "Location of Defect": "W2",
            "Signal of Defect": "",
            "Cause": "This alarm occurs when the voltage of the battery for backup of the encoder becomes lower than 2.8V. In case of the occurrence of this alarm, the alarm code is sent by the completion response for the first command after the alarm occurrence",
            "Potential Causes": [],
            "Sub-Code Description": "The sub code stands for the defective axis"
        }
    },
    "9109": {
        "0001": {
            "Message": "Hardware Reset Error [A1]",
            "Location of Defect": "A1",
            "Signal of Defect": "",
            "Cause": "No response for HRST command",
            "Potential Causes": [],
            "Sub-Code Description": ""
        }
    }
}
