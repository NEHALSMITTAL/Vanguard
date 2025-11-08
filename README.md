ArUco-Based Real-Time Event Classification & Geolocation Mapping

This project integrates CNN-based event classification, ArUco marker detection, and geospatial mapping using QGIS.
It performs real-time detection of five different event types, identifies the nearest ArUco marker, retrieves its latitude–longitude, and exports the results to a CSV file for mapping and analysis.

**
Project Overview**

-The project has two main modules:
1. Event Classification (CNN Model)
A deep learning model is trained to classify five different events using images captured in real time.
*Model Highlights
*Built using TensorFlow/Keras
*Uses Convolutional Neural Networks (CNN)

-Contains:
*Conv layers
*MaxPooling layers
*Dense layers
*Dropout layers to prevent overfitting
*Uses Categorical Cross-Entropy Loss for multi-class prediction
*Achieves real-time classification during camera feed inference

-Key Outputs
*Predicted event label
*Live display on top of the camera frame


2. ArUco Marker Detection + Nearest Marker Localization

This module detects ArUco markers placed on a top-down view setup, identifies their centers, and computes the nearest marker to the target marker (ID = 100).

Pipeline
1.Detect all markers using OpenCV ArUco module
2.Use corner refinement to improve sub-pixel accuracy
3.Compute centers for each detected marker
4.Calculate Euclidean distance between markers
5.Find nearest marker
6.Fetch its latitude and longitude from a CSV file
7.Append results to another CSV (“nearest_ids.csv”)
8.Import into QGIS to visualize the dynamic network/map



Tech Stack
Component	Technology
CNN--- Model	TensorFlow / Keras
ArUco--- Detection	OpenCV
Data Handling---	CSV
GIS Mapping ---	QGIS
Hardware---	Webcam, ArUco markers
Language---	Python

Project Structure
├── cnn_model_training.py        # Trains CNN on 5 event classes
├── cnn_live_prediction.py       # Runs real-time event detection
├── aruco_detection_mapping.py   # Detects ArUco markers + nearest ID mapping
├── lat_lon.csv                  # Contains ID, latitude, longitude
├── nearest_ids.csv              # Output CSV for QGIS mapping
├── README.md
└── requirements.txt

Model Summary
Feature     	Description
Input        	Images (resized depending on dataset)
Output	      5-class softmax predictions
Loss	        Categorical Cross-Entropy
Optimizer	     Adam
Regularization Dropout between Dense layers

Step 1 — Detect Event
CNN processes each frame → prints event label.
Step 2 — Detect ArUco Markers
OpenCV identifies ArUco markers from the top view.
Step 3 — Compute Nearest Marker
For the target marker (ID 100):
Find centers of all markers
Compute pixel-level Euclidean distance
Select nearest marker
Step 4 — Fetch GPS Coordinates
Reads the coordinates from lat_lon.csv.
Step 5 — Export to CSV
Each event + nearest marker is appended into:
nearest_ids.csv
Step 6 — Visualize on QGIS
Upload CSV → displays markers on geographic map.
ID,Latitude,Longitude
101,18.5204,73.8567
102,18.5212,73.8590

nearest_ids.csv (auto-generated)
Frame,Target_ID,Closest_ID,Latitude,Longitude
5,100,102,18.5212,73.8590
6,100,101,18.5204,73.8567

Features
*Real-time event classification
*Accurate ArUco detection with corner refinement
*Nearest-marker geospatial mapping
*Easy integration with GIS tools
*Fully automated pipeline
*Hardware-support ready

Future Enhancements
*Integrate YOLO-based marker detection
*Combine CNN + ArUco logic in single pipeline
*Add path planning using GPS coordinates
*Export to GeoJSON




