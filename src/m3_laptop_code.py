"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Jacob Murray.
  Spring term, 2018-2019.
"""
# Done 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m2_laptop_code as m2


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Jacob Murray")
    frame_label.grid()
    # Done 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    arm_up_button = ttk.Button(frame, text='Arm Up')
    arm_up_button.grid(row = 0, column = 0)
    arm_up_speed = ttk.Entry(frame, width = 8)
    arm_up_speed.insert(0, '100')
    arm_up_speed.grid(row = 0, column = 1)
    arm_up_button["command"] = lambda: handle_arm_up(arm_up_speed.get(), mqtt_sender)

    calibrate_arm_button = ttk.Button(frame, text='Calibrate Arm')
    calibrate_arm_button.grid(row = 1, column = 0)
    arm_calibrate_speed = ttk.Entry(frame, width=8)
    arm_calibrate_speed.insert(0, '100')
    arm_calibrate_speed.grid(row = 1, column = 1)
    calibrate_arm_button["command"] = lambda: handle_arm_calibrate(arm_calibrate_speed.get(), mqtt_sender)

    arm_to_button = ttk.Button(frame, text='Move Arm')
    arm_to_button.grid(row = 2, column = 0)
    arm_to_speed = ttk.Entry(frame, width = 8)
    arm_to_speed.insert(0, '100')
    arm_to_speed.grid(row = 2, column = 2)
    arm_to_position = ttk.Entry(frame, width = 8)

    arm_to_position.grid(row = 2, column = 1)
    arm_to_button["command"] = lambda: handle_arm_to(arm_to_position.get(), arm_to_speed.get(), mqtt_sender)

    arm_down_button = ttk.Button(frame, text='Arm Down')
    arm_down_button.grid(row = 3, column = 0)
    arm_down_speed = ttk.Entry(frame, width = 8)
    arm_down_speed.insert(0, '100')
    arm_down_speed.grid(row = 3, column = 1)
    arm_down_button["command"] = lambda: handle_arm_down(arm_down_speed.get(), mqtt_sender)

    # Return your frame:
    return frame


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.
def handle_arm_up(arm_up_speed, mqtt_sender):
    speed = arm_up_speed.get()
    print('arm_up message:', arm_up_speed)
    mqtt_sender.send_message('arm_up', [speed])


def handle_arm_calibrate(arm_calibrate_speed, mqtt_sender):
    speed = arm_calibrate_speed.get()
    print('arm_calibrate message:', speed)
    mqtt_sender.send_message('arm_calibrate', [speed])


def handle_arm_to(arm_to_speed, mqtt_sender):
    speed = arm_to_speed.get()
    print('arm_to message:', speed)
    mqtt_sender.send_message('arm_to', [speed])


def handle_arm_down(arm_down_speed, mqtt_sender):
    speed = arm_down_speed.get()
    print('arm_down message:', speed)
    mqtt_sender.send_message('arm_down', [speed])
