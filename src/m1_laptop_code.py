"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Josh Krsek.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Josh Krsek")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    forward_dist_button = ttk.Button(frame, text="Go Forward Distance")
    backward_dist_button = ttk.Button(frame, text="Go Backward Distance")
    forward_inches_label = ttk.Label(frame, text="Inches")
    backward_inches_label = ttk.Label(frame, text="Inches")
    forward_inches = ttk.Entry(frame, width=6)
    backward_inches = ttk.Entry(frame, width=6)
    forward_speed_label = ttk.Label(frame, text="Speed")
    forward_speed = ttk.Entry(frame, width=6)
    backward_speed_label = ttk.Label(frame, text="Speed")
    backward_speed = ttk.Entry(frame, width=6)

    forward_dist_button.grid(row=3, column=0)
    backward_dist_button.grid(row=7, column=0)
    forward_inches_label.grid(row=3, column=2)
    backward_inches_label.grid(row=7, column=2)
    forward_inches.grid(row=4, column=2)
    backward_inches.grid(row=8,column=2)
    forward_speed_label.grid(row=3, column=4)
    forward_speed.grid(row=4, column=4)
    backward_speed_label.grid(row=7, column=4)
    backward_speed.grid(row=8, column=4)

    forward_dist_button["command"] = lambda: go_forward(forward_inches, forward_speed, mqtt_sender)


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
def go_forward(forward_inches, forward_speed, mqtt_sender):
    inches = int(forward_inches.get())
    speed = int(forward_speed.get())
    print()
    print('Sending a message to the robot to go forward', inches,'inches forward at a speed of', speed)
    mqtt_sender.send_message('forward',[inches, speed])