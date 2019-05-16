"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jacob Murray.
  Spring term, 2018-2019.
"""
# Done 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m1_robot_code as m1
import m2_robot_code as m2


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

    # TODO: Add methods here as needed.
    def arm_up(self, speed):
        print_message_received('arm_up', [speed])
        self.robot.arm_and_claw.motor.turn_on(speed)
        while True:
            ans = self.robot.arm_and_claw.touch_sensor.is_pressed()
            if ans == True:
                self.robot.arm_and_claw.motor.turn_off()
                break

    def arm_calibrate(self, speed):
        print_message_received('arm_calibrate', [speed])
        self.arm_up(speed)
        self.robot.arm_and_claw.motor.turn_on(-speed)
        while True:
            ans_deg = self.robot.arm_and_claw.motor.get_position()
            if float(ans_deg) <= 14.2 * 360:
                self.robot.arm_and_claw.motor.turn_off()
                self.robot.arm_and_claw.motor.reset_position()
                break

    def arm_to(self, position, speed):
        print_message_received('arm_to', [position])
        start_pos = self.robot.arm_and_claw.motor.get_position()
        if float(start_pos) <= position:
            self.robot.arm_and_claw.motor.turn_on(speed)
            while True:
                cur_pos = self.robot.arm_and_claw.motor.get_position()
                if float(cur_pos) >= position:
                    self.robot.arm_and_claw.motor.turn_off()
                    break
        else:
            self.robot.arm_and_claw.motor.turn_on(-speed)
            while True:
                cur_pos = self.robot.arm_and_claw.motor.get_position()
                if float(cur_pos) <= position:
                    self.robot.arm_and_claw.motor.turn_off()
                    break

    def arm_down(self, speed):
        print_message_received('arm_down', [speed])
        self.arm_to(0, speed)












def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

