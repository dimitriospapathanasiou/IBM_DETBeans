from datetime import datetime, timedelta


def calculate_taxi_demand(arrival_time, arrival_delay, fleet_size):
    passengers_per_flight = 7
    arrival_time = datetime.strptime(arrival_time, "%H:%M")

    # Adjusting arrival time based on delay
    arrival_time += timedelta(minutes=arrival_delay)

    time_frames = []
    current_time = datetime.strptime("00:00", "%H:%M")
    while current_time < datetime.strptime("23:59", "%H:%M"):
        time_frames.append(current_time.strftime("%H:%M"))
        current_time += timedelta(minutes=15)

    demand_per_time_frame = {}
    for time_frame in time_frames:
        demand = 0
        if (arrival_time.hour == int(time_frame[:2]) and
                int(time_frame[3:]) <= arrival_time.minute < int(time_frame[3:]) + 15):
            for i in range(fleet_size):
                demand += passengers_per_flight
        demand_per_time_frame[time_frame] = demand

    return demand_per_time_frame


multiple_flights_data = [
    {"arrival_time": "08:00", "arrival_delay": 0, "fleet_size": 8},
    {"arrival_time": "10:30", "arrival_delay": 30, "fleet_size": 12},
    {"arrival_time": "13:45", "arrival_delay": 15, "fleet_size": 6},
    {"arrival_time": "16:20", "arrival_delay": 0, "fleet_size": 10},
    {"arrival_time": "19:55", "arrival_delay": 45, "fleet_size": 5},
    {"arrival_time": "21:30", "arrival_delay": 10, "fleet_size": 8},
    {"arrival_time": "23:15", "arrival_delay": 20, "fleet_size": 7},
    {"arrival_time": "03:45", "arrival_delay": 10, "fleet_size": 5},
    {"arrival_time": "09:20", "arrival_delay": 5, "fleet_size": 7},
    {"arrival_time": "11:55", "arrival_delay": 25, "fleet_size": 9},
    {"arrival_time": "14:30", "arrival_delay": 0, "fleet_size": 6},
    {"arrival_time": "17:15", "arrival_delay": 15, "fleet_size": 8},
    {"arrival_time": "02:40", "arrival_delay": 30, "fleet_size": 4},
    {"arrival_time": "22:25", "arrival_delay": 20, "fleet_size": 10},
    {"arrival_time": "05:25", "arrival_delay": 20, "fleet_size": 10},
    {"arrival_time": "06:15", "arrival_delay": 15, "fleet_size": 6},
    {"arrival_time": "09:45", "arrival_delay": 0, "fleet_size": 8},
    {"arrival_time": "12:20", "arrival_delay": 10, "fleet_size": 5},
    {"arrival_time": "15:55", "arrival_delay": 20, "fleet_size": 7},
    {"arrival_time": "18:30", "arrival_delay": 5, "fleet_size": 9},
    {"arrival_time": "01:10", "arrival_delay": 30, "fleet_size": 12},
    {"arrival_time": "03:55", "arrival_delay": 0, "fleet_size": 10},
    {"arrival_time": "07:35", "arrival_delay": 15, "fleet_size": 6},
    {"arrival_time": "10:05", "arrival_delay": 25, "fleet_size": 8},
    {"arrival_time": "13:40", "arrival_delay": 10, "fleet_size": 7},
    {"arrival_time": "16:25", "arrival_delay": 20, "fleet_size": 9},
    {"arrival_time": "19:50", "arrival_delay": 0, "fleet_size": 8},
    {"arrival_time": "22:15", "arrival_delay": 45, "fleet_size": 5},
]

total_demand_per_time_frame = {time_frame: 0 for time_frame in calculate_taxi_demand("00:00", 0, 1)}

for flight_data in multiple_flights_data:
    demand_per_time_frame = calculate_taxi_demand(flight_data["arrival_time"], flight_data["arrival_delay"],
                                                  flight_data["fleet_size"])
    for time_frame, demand in demand_per_time_frame.items():
        total_demand_per_time_frame[time_frame] += demand

print("Demand for taxis for each time frame (for all flights):")
for time_frame, demand in total_demand_per_time_frame.items():
    print(f"{time_frame}: {demand}")
