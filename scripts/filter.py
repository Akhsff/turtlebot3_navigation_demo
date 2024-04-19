#!/usr/bin/env python3

#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
    filtered_ranges = []
    for i in range(len(data.ranges)):
        # Замена NaN и Inf на -1, а также значений вне диапазона
        if not rospy.is_shutdown():
            if data.ranges[i] == float('inf') or data.ranges[i] == float('NaN') or data.ranges[i] != data.ranges[i] or data.ranges[i] < data.range_min or data.ranges[i] > data.range_max:
                filtered_ranges.append(-1)
            else:
                filtered_ranges.append(data.ranges[i])
    # Создание нового сообщения LaserScan для публикации
    filtered_scan = LaserScan()
    filtered_scan.header = data.header
    filtered_scan.angle_min = data.angle_min
    filtered_scan.angle_max = data.angle_max
    filtered_scan.angle_increment = data.angle_increment
    filtered_scan.time_increment = data.time_increment
    filtered_scan.scan_time = data.scan_time
    filtered_scan.range_min = data.range_min
    filtered_scan.range_max = data.range_max
    filtered_scan.ranges = filtered_ranges
    filtered_scan.intensities = data.intensities

    # Публикация отфильтрованных данных
    pub.publish(filtered_scan)

def listener():
    rospy.init_node('scan_filter', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('/scan/filtered', LaserScan, queue_size=10)
    listener()
