#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Глобальные переменные
prev_distance = None
direction = "Stationary"

def calculate_distance(data, angle_range):
    # Фильтрация и вычисление среднего расстояния в заданном секторе
    valid_ranges = [r for r in data.ranges if r > 0]
    if len(valid_ranges) > 0:
        return np.mean(valid_ranges)
    else:
        return None

def update_direction(current_distance):
    global prev_distance, direction
    if prev_distance is not None:
        if abs(current_distance - prev_distance) < 0.02:
            direction = "Stationary"
        elif current_distance > prev_distance:
            direction = "Moving Away"
        else:
            direction = "Approaching"
    prev_distance = current_distance

def callback(data):
    global direction
    # Вычисляем расстояние до препятствия
    current_distance = calculate_distance(data, angle_range=(5, 10))
    if current_distance is not None:
        update_direction(current_distance)
        rospy.loginfo(f"Distance: {current_distance} m, Direction: {direction}")

def animate(i):
    plt.cla()
    plt.xlim(-5, 5)
    plt.ylim(-1, 10)
    plt.plot(0, 0, 'bo', label='Robot')  # Робот в центре
    if prev_distance is not None:
        plt.plot(prev_distance, 0, 'rs', label='Obstacle')  # Препятствие
    plt.legend()
    plt.title(f"Distance: {prev_distance} m, Direction: {direction}")

def listener():
    rospy.init_node('distance_and_direction', anonymous=True)
    rospy.Subscriber('/scan/filtered', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    # Визуализация
    fig = plt.figure()
    ani = FuncAnimation(fig, animate, interval=1000)
    plt.show(block=False)

    listener()
