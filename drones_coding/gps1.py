import rospy
from clover import srv
from std_srvs.srv import Trigger
import math

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
land = rospy.ServiceProxy('land', Trigger)

def arrival_wait(tolerance=0.2):

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

# print(get_telemetry())
start = get_telemetry()

navigate(x= 0, y=0, z=3, frame_id = 'body', auto_arm=True)
arrival_wait()

navigate_global(lat=start.lat + 1.0/60/60, lon = start.lon, z=start.z+3, speed=1)
arrival_wait()

land()



