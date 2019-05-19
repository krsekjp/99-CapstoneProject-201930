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
import math

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

    def spinr(self,speed_right,distance_right):
        print('spinr')
        speed = speed_right
        self.robot.drive_system.right_motor.reset_position()
        while True:
            #THIS IS A TEST#print((self.robot.drive_system.right_motor.get_position()))
            self.robot.drive_system.right_motor.turn_on(-speed_right)
            self.robot.drive_system.left_motor.turn_on(speed_right)
            self.robot.drive_system.go(speed, -speed)
            number_rotations = int(self.robot.drive_system.right_motor.get_position())
            if (-1*number_rotations) >= (int(distance_right)*4.75):
                self.robot.drive_system.stop()
                break

    def spinl(self,speed_left,distance_left):
        print('spinl')
        speed = speed_left
        self.robot.drive_system.left_motor.reset_position()
        while True:
            #THIS IS A TEST#print((self.robot.drive_system.left_motor.get_position()))
            self.robot.drive_system.left_motor.turn_on(-speed_left)
            self.robot.drive_system.right_motor.turn_on(speed_left)
            self.robot.drive_system.go(-speed, speed)
            number_rotations = int(self.robot.drive_system.left_motor.get_position())
            if (-1*number_rotations) >= (int(distance_left)*4.75):
                self.robot.drive_system.stop()
                break
    def spinf(self,area,speed,delta):
        print('spin_f')
        while True:
            self.robot.drive_system.right_motor.turn_on(-speed)
            self.robot.drive_system.left_motor.turn_on(speed)
            self.robot.drive_system.go(speed, -speed)
            ###THis is a Test###print(self.robot.sensor_system.camera.get_biggest_blob().get_area())
            object = self.robot.sensor_system.camera.get_biggest_blob()
            #Test print(object.center.x)
            if self.robot.sensor_system.camera.get_biggest_blob().get_area() >= area:
                object = self.robot.sensor_system.camera.get_biggest_blob()
                if delta <= math.fabs(object.center.x-150):
                    self.robot.drive_system.stop()
                    self.Tone()
                    self.robot.sound_system.speech_maker.speak('You Did it!')
                    break



    def Tone(self):
        print('You did it! Congrats!')
        self.robot.sound_system.beeper.beep()
        return



def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.
