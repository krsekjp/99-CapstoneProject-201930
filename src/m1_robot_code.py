"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Josh Krsek.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

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

    def go(self, left_motor_speed, right_motor_speed):
        """ Tells the robot to go (i.e. move) using the given motor speeds. """
        print_message_received("go", [left_motor_speed, right_motor_speed])
        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

    # TODO: Add methods here as needed.

    def forward(self, inches, speed):
        print_message_received('forward',[inches, speed])
        self.robot.drive_system.right_motor.reset_position()
        self.robot.drive_system.go(speed, speed)
        while True:
            print(self.robot.drive_system.right_motor.get_position())
            if self.robot.drive_system.right_motor.get_position() >= inches*90:
                break
        self.robot.drive_system.stop()

    def backward(self, inches, speed):
        print_message_received('backward',[inches, speed])
        self.robot.drive_system.right_motor.reset_position()
        self.robot.drive_system.go(-speed, -speed)
        while True:
            print(self.robot.drive_system.right_motor.get_position())
            if self.robot.drive_system.right_motor.get_position() <= -inches*90:
                break
        self.robot.drive_system.stop()

    def go_until_dist(self, x, delta, speed):
        print_message_received('go_until_dist',[x, delta, speed])
        self.robot.drive_system.go(speed,speed)
        while True:
            five_readings = []
            for _ in range(5):
                dist_from = self.robot.sensor_system.ir_proximity_sensor.get_distance()
                five_readings = five_readings + [dist_from]
            #print(five_readings)
            biggest = max(five_readings)
            smallest = min(five_readings)
            five_readings.remove(biggest)
            five_readings.remove(smallest)
            sum_of_3 = sum(five_readings)
            av_of_3 = sum_of_3/3
            print(av_of_3)
            if av_of_3 <= x+delta:
                break
        self.robot.drive_system.stop()

def print_message_received(method_name, arguments):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

