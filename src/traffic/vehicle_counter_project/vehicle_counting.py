import cv2
import glob
import os
from vehicle_detector import VehicleDetector

def program():
    vd = VehicleDetector()
    vehicles_folder_count = 0
    img = cv2.imread("images/18.jpg")
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    vehicles_folder_count += vehicle_count

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

    cv2.imshow("Cars", img)
    cv2.waitKey(1)

    os.system("PAUSE")

    print("Total current count", vehicles_folder_count)

if __name__ == "__main__":
    try:
        program()
    except:
        print("[EXIT]")
        exit(0)

