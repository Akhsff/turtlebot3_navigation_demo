## Build and Run

1. Запустить симуляцию Gazebo:

   ```bash
   roslaunch turtlebot3_navigation_demo turtlebot3_wall.launch 
   ```

2. Слушать данные с лидара

   ```bash
   rostopic echo /scan
   ```

3. Управление с клавиатуры:

   ```bash
   roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
   ```

4. Фильтрация данных с лидара согласно заданию:

   ```bash
   rosrun turtlebot3_navigation_demo filter.py
   rostopic echo scan/filtered
   ```

5. Определяем направление движения
   
   ```bash
   rosrun turtlebot3_navigation_demo visual.py 
   ```
