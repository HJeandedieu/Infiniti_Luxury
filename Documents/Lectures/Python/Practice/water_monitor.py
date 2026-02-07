moisture_levels = [35, 42, 48, 55, 61, 79, 84, 92, 87, 70, 58, 45]

# Threshold configuration (percentages)
moisture_low_threshold = 40
moisture_medium_threshold = 60
moisture_high_threshold = 80

temperature_low_threshold = 20
temperature_medium_threshold = 30
temperature_high_threshold = 40

valve_control = False

# VARIABLES TO STORE THE MESSAGES AND THE ALERT LEVEL
high_alert_count= 0
alert_log = []

# OUTPUT
print("Water Sensor System Starting...")
print(f"Monitoring {len(moisture_levels)} readings throughout the day.")
for index, moisture in enumerate(moisture_levels):
    hour = 6 + (2 * index)
    print(f"{hour}:00 - Moisture: {moisture}% ")
    if moisture < moisture_low_threshold:
        status = "LOW"
        message = f"Low moisture detected at {hour}:00"
        alert_log.append(message)
    elif moisture <= moisture_medium_threshold:
        status = "NORMAL"
    elif moisture <= moisture_high_threshold:
        status = "MODERATE"
        message = f"Moisture increased at {hour}:00"
        alert_log.append(message)
    else :
        status = "HIGH"
        message = f" CRITICAL High moisture detected at {hour}:00 ({moisture}%)"
        alert_log.append(message)
        high_alert_count = high_alert_count +1
    print(f"  Status: {status}")


#CONTINOUS MONITOR SYSTEM
print("Starting Continuous Monitor Mode(once per hour)...")
import random
danger_index = 0
while high_alert_count > 0:
    danger_index += 1
    simulated_moisture = random.randint(30, 95)
    simulated_temperature = random.randint(20, 40)
    print(f"[{danger_index}]Simulated Hourly Reading: {simulated_moisture}%", end=" | ")

    if simulated_moisture > moisture_high_threshold and simulated_temperature > temperature_high_threshold:
        print("DANGER -  High Evaporation Risk")
        high_alert_count += 1
    elif simulated_moisture < moisture_low_threshold:
        print("Keep irrigation active.")
    else:
        print("Conditions Stable.")
    if high_alert_count >= 3:
        print("[Valve Shutoff Activated]")
        break

    if danger_index >= 10:
        print("Monitoring Paused after 10 simulated hours ")
        break
    else:
        print("Monitoring Paused ")  #Once the normal conditions are met


# REPORT SUMMARY
print("DAILY SUMMARY")
print(f"Total readings recorded: {len(moisture_levels)}")
print(f"High moisture alerts: {high_alert_count}")
print(f"Logged Alerts: {len(alert_log)}")

if alert_log:
    print("Log: ")
    for a in alert_log:
        print(f"    - {a}")
else:
    print("No alerts logged.")
    print("Healthy water levels maintained")

