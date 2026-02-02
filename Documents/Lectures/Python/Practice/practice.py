# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         return print("Hello my name is",self.name)
#
# alice = Student("Alice", 22)
# alice.greet()

# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.age = age

# class Person:
#     def greet(self):
#         return "Hello, I am a person"
# class Student(Person):
#     def greet(self):
#         base = super().greet()
#         return base + " and I am studying"
# s = Student()
# print(s.greet())
# print(Student.greet(s))

# class Person:
#     def __init__(self):
#         print("Person init")
#
# class Learner:
#     def __init__(self):
#         print("Learner init")
#
#
# class Student(Person, Learner):
#     def __init__(self):
#         super().__init__()
#         print("Student init")
#
# s = Student()
#
# print(Student.mro())

# class Person:
#     def __init__(self):
#         super().__init__()
#         print("Person init")
#
# class Learner:
#     def __init__(self):
#         super().__init__()
#         print("Learner init")
#
# class Student(Person, Learner):
#     def __init__(self):
#         super().__init__()
#         print("Student init")
#
# s = Student()

# class A:
#     def __init__(self):
#         print("A init")

# D init
# B init
# A init
# C init
# A init


#FLOW CONTROL STRUCTURES

# x = int(input("Enter Number: "))
# if x < 0:
#     print(f"The number {x} you entered is negative")
#     if x % 2 == 0:
#         print(f"The number {x} you entered is even")
#     elif x % 2 == 1:
#         print(f"The number {x} you entered is odd")
# elif x > 0:
#     print(f"The number {x} you entered is positive")
#     if x % 2 == 0:
#         print(f"The number {x} you entered is even")
#     elif x % 2 == 1:
#         print(f"The number {x} you entered is odd")

# x = list(range(16))
# y = list(range(16, 31))
#
# combination = tuple(zip(x,y))
# print(combination)
#
#
# for point in combination:
#     match point:
#         case (0, 0):
#             print("Origin")
#         case (0, y):
#             print(f"Y = {y}")
#         case (x, 0):
#             print(f"X={x}")
#         case (x, y):
#             print(f"X={x}, Y={y}")
#         case _:
#             raise ValueError("Not a point")

# class Point:
#     __match_args__ = ('x', 'y')
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# points = [Point(2, 5)]
# match points:
#     case []:
#         print("No points")
#     case [Point(0, 0)]:
#         print("The origin")
#     case [Point(x, y)]:
#         print(f"Single point {x}, {y}")
#     case [Point(0, y1), Point(0, y2)]:
#         print(f"Two on the Y axis at {y1}, {y2}")
#     case _:

#
# from pathlib import Path
#
# file_path = Path("folder") / "subfolder" / "file.txt"
#
# print(file_path)
#
# print(file_path.parent)
# print(file_path.name)
# print(file_path.suffix)
# print(file_path.stem)
#
#
# print(file_path.exists())
#
# print(file_path.resolve())

#
# REQUIRED_FIELDS = {
#     "device": str,
#     "value": (int,float),
#     "timestamp": str
# }
#
# def validate_payload(data):
#     if not isinstance(data, dict):
#         raise ValueError(f"Missing require field: {field}")
#
#     for field, expected_value in REQUIRED_FIELDS.items():
#         if field not in data:
#             raise ValueError(f"Missing required field: {field}")
#
#         if not isinstance(data[field], expected_value):
#             raise ValueError(f"{field} must be of type {expected_value}")
#
#     if data["value"] < 0:
#         raise ValueError("Sensor data can't be negative")
#
#     if len(data["device"]) == 0:
#         raise ValueError("Device name can't be empty")

import numpy as np

sensor_data = np.array([
    [85, 24.5, 101.3], [82, 23.8, 101.2], [78, 23.0, 101.1], [75, 22.5, 101.0],
    [73, 22.0, 100.9], [72, 21.8, 100.8], [70, 21.5, 100.7], [69, 21.2, 100.6],
    [68, 21.0, 100.5], [67, 20.8, 100.4], [66, 20.6, 100.3], [65, 20.4, 100.2],
    [64, 20.2, 100.1], [63, 20.0, 100.0], [62, 19.8, 99.9], [61, 19.6, 99.8],
    [75, 26.0, 102.0], [88, 29.5, 103.5], [92, 31.0, 104.0], [95, 32.0, 104.5],
    [94, 31.5, 104.2], [90, 30.0, 103.0], [87, 28.5, 102.5], [86, 27.0, 102.0]
])

print("Sensor data shape:", sensor_data.shape)
print("First few readings (hourly):", sensor_data[:5])


#Calculate total daily averages (mean), std dev, and max for each row(hour)
daily_mean = sensor_data.mean(axis = 0)          #Mean across hours(per sensor)
daily_std = sensor_data.std(axis = 0)            #Standard deviation
daily_max = sensor_data.max(axis = 0)            #Max value across all hours(per sensor)
daily_min = sensor_data.min(axis = 0)            #Min value



print("----Daily Statistics Per Sensor ----")
print("Mean (Moisture, Temp, Pressure):", np.round(daily_mean, 2))
print("Std Dev:", np.round(daily_std, 2))
print("Max:", np.round(daily_max, 2))
print("Min:", np.round(daily_min, 2))


#   DEFINING THRESHOLD VALUES

moist_threshold = 90
temp_threshold = 30


# Vectorized comparisons

high_moisture = sensor_data[:,0] > moist_threshold
high_temp = sensor_data[:,1] > temp_threshold
any_high_risk =  high_moisture | high_temp

print("High Risk Flags (Hour - Risk True/False):")
for i in range(len(any_high_risk)):
    risk_str = 'YES' if any_high_risk[i] else 'NO'
    print(f"Hour {i+1:2d}: Moist = {sensor_data[i,0]:3.0f}% | Risk = {risk_str}")


#Moisture readings only

moisture = sensor_data[:,0]
#Use convolution to compute rolling mean over 4-hour window
window_size = 4
rolling_kernel = np.ones(window_size)
rolling_avg = np.convolve(moisture, rolling_kernel, mode="valid")

print('Moisture trend analysis: ')
print("Original (first 6): ", np.round(rolling_avg[:6], 1))

#Note: rolling_avg has length = 24 -4 + 1 = 21

print(f"Rolling data starts at hour {window_size}")



#compute delta (change) between adjacent hours

delta_moisture = np.diff(moisture, n=1) # n=1 → first derivative
delta_moisture_abrupt = delta_moisture > 10 # Flag if change > 10% per hour

print("Hour-to-hour change in moisture (first 10): ")
# Define threshold for an "abrupt" change
threshold = 1.0  # percent

print("Hour-to-hour change in moisture (first 10, significant only):")
for i in range(10):
    change = delta_moisture[i]
    # Only mark as ABRUPT if change exceeds threshold
    abrupt = "ABRUPT !" if abs(change) >= threshold else ""
    print(f"Hour {i+1} →{i+2}: {change:+5.1f}% {abrupt}")
