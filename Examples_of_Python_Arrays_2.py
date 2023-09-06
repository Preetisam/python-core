from array import array

# Create an array of temperature measurements (floats)
temperature_data = array('f', [23.5, 24.0, 22.8, 25.2, 23.7])

# Calculate the average temperature
average_temperature = sum(temperature_data) / len(temperature_data)

# Find the maximum temperature
max_temperature = max(temperature_data)

# Print the results
print("Temperature Data:")
print(temperature_data)
print(f"Average Temperature: {average_temperature}°C")
print(f"Maximum Temperature: {max_temperature}°C")
