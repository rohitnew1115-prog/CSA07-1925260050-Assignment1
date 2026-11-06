
# TASK 1: Traffic Analysis
# Smart Manufacturing Plant Network

print("=" * 55)
print(" SMART MANUFACTURING PLANT - TRAFFIC ANALYSIS")
print("=" * 55)

# 1. Robot Controller Traffic
robots = 40
robot_data_bytes = 200
robot_interval_ms = 2

robot_commands_per_second = 1000 / robot_interval_ms
robot_bandwidth_per_robot = (
    robot_commands_per_second * robot_data_bytes * 8
) / 1_000_000

total_robot_bandwidth = robots * robot_bandwidth_per_robot

# 2. Vibration Sensor Traffic
sensors = 600
sensor_data_bytes = 50

total_sensor_bandwidth = (
    sensors * sensor_data_bytes * 8
) / 1_000_000

# 3. CCTV Camera Traffic
cameras = 24
camera_bandwidth_mbps = 4

total_cctv_bandwidth = cameras * camera_bandwidth_mbps

# 4. Office User Traffic
office_users = 150
office_peak_mbps = 2
active_percentage = 10

active_office_users = office_users * active_percentage / 100

total_office_bandwidth = (
    active_office_users * office_peak_mbps
)

# 5. Calculate Total Bandwidth
total_bandwidth = (
    total_robot_bandwidth
    + total_sensor_bandwidth
    + total_cctv_bandwidth
    + total_office_bandwidth
)

# Display Results
print("\n1. ROBOT CONTROLLER TRAFFIC")
print(f"Number of robots: {robots}")
print(f"Commands per second per robot: {robot_commands_per_second:.0f}")
print(f"Bandwidth per robot: {robot_bandwidth_per_robot:.3f} Mbps")
print(f"Total robot bandwidth: {total_robot_bandwidth:.3f} Mbps")

print("\n2. VIBRATION SENSOR TRAFFIC")
print(f"Number of sensors: {sensors}")
print(f"Total sensor bandwidth: {total_sensor_bandwidth:.3f} Mbps")

print("\n3. CCTV CAMERA TRAFFIC")
print(f"Number of cameras: {cameras}")
print(f"Bandwidth per camera: {camera_bandwidth_mbps} Mbps")
print(f"Total CCTV bandwidth: {total_cctv_bandwidth:.3f} Mbps")

print("\n4. OFFICE USER TRAFFIC")
print(f"Total office users: {office_users}")
print(f"Active users: {active_office_users:.0f}")
print(f"Total office bandwidth: {total_office_bandwidth:.3f} Mbps")

print("\n" + "=" * 55)
print(f"TOTAL REQUIRED BANDWIDTH: {total_bandwidth:.3f} Mbps")
print("=" * 55)
