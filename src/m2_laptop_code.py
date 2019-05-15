"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Colton McKay.
  Spring term, 2018-2019.
"""
# DONE:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Colton McKay")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

#SPRINT 1
    spin_left_button = ttk.Button(frame, text = 'Spin Left')
    spin_left_button.grid(row = 0, column = 0)

    spin_left_button['command'] = lambda: spin_left(entry_box_left_speed, entry_box_left_distance, mqtt_sender)

    entry_box_left_speed = ttk.Entry(frame)
    entry_box_left_speed.insert(0,'100')
    entry_box_left_speed.grid(row=1,column=0)

    entry_box_left_distance = ttk.Entry(frame)
    entry_box_left_distance.grid(row=2, column=0)

############ Left^ ################## Right V ############

    spin_right_button = ttk.Button(frame, text = 'Spin Right')
    spin_right_button.grid(row = 0, column = 1)\

    spin_right_button['command'] = lambda: spin_right(entry_box_right_speed,entry_box_right_distance,mqtt_sender)

    label_speed_r = ttk.Label(frame, text='Speed from 0 to 100')
    label_speed_r.grid(row=1, column= 2)
    label_distance_r = ttk.Label(frame, text="Distance (in Degrees)")
    label_distance_r.grid(row=2, column=2)

    entry_box_right_distance = ttk.Entry(frame)
    entry_box_right_distance.grid(row=2, column=1)

    entry_box_right_speed = ttk.Entry(frame)
    entry_box_right_speed.insert(0, '100')
    entry_box_right_speed.grid(row=1, column=1)
###########################################################



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
#def spin_left(speed_l,distance_l):


def spin_right(right_speed, right_distance):
    speed_right = int(right_speed.get())
    distance_right = int(right_distance.get())
    mqtt.send_message('spinr',speed_right,distance_right)

def spin_left(left_speed, left_distance):
    speed_left = int(left_speed.get())
    distance_left = int(left_distance.get())
    mqtt.send_message('spinl',speed_left,distance_left)