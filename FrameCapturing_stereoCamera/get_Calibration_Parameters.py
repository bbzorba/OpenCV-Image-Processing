from pyzed import sl

# Create a ZED camera object
zed = sl.Camera()

# Set configuration parameters
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD720
init_params.camera_fps = 30

# Open the camera
err = zed.open(init_params)
if err != sl.ERROR_CODE.SUCCESS:
    exit(-1)

calibration_params = zed.get_camera_information().camera_configuration.calibration_parameters_raw
fx_left = calibration_params.left_cam.fx
fy_left = calibration_params.left_cam.fy
cx_left = calibration_params.left_cam.cx
cy_left = calibration_params.left_cam.cy
k1_left = calibration_params.left_cam.disto[0]
k2_left = calibration_params.left_cam.disto[1]
k3_left = calibration_params.left_cam.disto[2]
p1_left = calibration_params.left_cam.disto[3]
p2_left = calibration_params.left_cam.disto[4]
h_fov_left = calibration_params.left_cam.h_fov

translation = calibration_params.T[2]

fx_right = calibration_params.right_cam.fx
fy_right = calibration_params.right_cam.fy
cx_right = calibration_params.right_cam.cx
cy_right = calibration_params.right_cam.cy
k1_right = calibration_params.right_cam.disto[0]
k2_right = calibration_params.right_cam.disto[1]
k3_right = calibration_params.right_cam.disto[2]
p1_right = calibration_params.right_cam.disto[3]
p2_right = calibration_params.right_cam.disto[4]
h_fov_right = calibration_params.right_cam.h_fov

print("calibration parameters for left camera:")
print("fx_left: " ,fx_left)
print("fy_left: " ,fy_left)
print("cx_left: " ,cx_left)
print("cy_left: " ,cy_left)
print("k1_left: " ,k1_left)
print("k2_left: " ,k2_left)
print("k3_left: " ,k3_left)
print("p1_left: " ,p1_left)
print("p2_left: " ,p2_left)
print("hfov_left: ", h_fov_left)

print("Translation between left and right eye on z-axis: ",translation)

print("calibration parameters for right camera:")
print("fx_right: " ,fx_right)
print("fy_right: " ,fy_right)
print("cx_right: " ,cx_right)
print("cy_right: " ,cy_right)
print("k1_right: " ,k1_right)
print("k2_right: " ,k2_right)
print("k3_right: " ,k3_right)
print("p1_right: " ,p1_right)
print("p2_right: " ,p2_right)
print("hfov_right: ", h_fov_right)