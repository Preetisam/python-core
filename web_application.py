# Dictionary to store cached data
cache = {}

def get_data_from_cache(key):
    if key in cache:
        print(f"Getting data for key '{key}' from cache.")
        return cache[key]
    else:
        print(f"Data for key '{key}' not found in cache.")
        return None

# Simulating caching data
data = [1, 2, 3, 4]
cache["my_data"] = data

# Using the get_data_from_cache function
requested_data = get_data_from_cache("my_data")
if requested_data is data:
    print("Using cached data.")
else:
    print("Data not in cache. Fetching from source and caching.")
data.append(5)

requested_data = get_data_from_cache("my_data")
if requested_data is data:
    print("Using cached data.")
else:
    print("Data not in cache. Fetching from source and caching.")
#The is operator returns True if cached data remains unchanged, 
#demonstrating object identity in practical scenarios like caching.
