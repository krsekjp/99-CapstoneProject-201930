"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Colton McKay.
  Spring term, 2018-2019.
"""
# DONE:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m2_robot_code as m2
import m3_robot_code as m3


class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot code

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def stop(self):
        """ Tells the robot to stop moving. """
        print_message_received("stop")
        self.robot.drive_system.stop()

    # TODO: Add methods here as needed.

    def spinr(self,right_speed,right_distance):
        self.robot.drive_system.right_motor.reset_position()
        speed = right_speed
        self.robot.drive_system.right_motor.turn_on()
        self.robot.drive_system.go(0,speed)
        number_rotations = int(self.robot.drive_system.right_motor.get_position())
        while True:
            if number_rotations >= right_distance:
                break

    def spinl(self,left_speed,left_distance):
        speed = left_speed
        self.robot.drive_system.left_motor.reset_position()
        self.robot.drive_system.left_motor.turn_on()
        self.robot.drive_system.go(speed,0)
        number_rotations = int(self.robot.drive_system.left_motor.get_position())
        while True:
            if number_rotations >= left_distance:
                break

def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.


