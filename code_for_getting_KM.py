import pandas as pd
from geopy.distance import geodesic

# Load the DataFrame from the Excel file
df = pd.read_excel('daft_listings_with_coordinates.xlsx')

# Dublin city center coordinates
dublin_center_coords = (53.349805, -6.26031)

# Function to calculate distance between two sets of coordinates in kilometers
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

# Calculate distances for each row and store them in a list
distances = []
for index, row in df.iterrows():
    property_coords = (row['Latitude'], row['Longitude'])
    distance = calculate_distance(property_coords, dublin_center_coords)
    # Apply an 8% offset to the distance
    distance_with_offset = distance * 1.08
    distances.append(distance_with_offset)

# Add distances to DataFrame as a new column
df['Distance to Dublin City Center (km)'] = distances

# Save the updated DataFrame to the Excel file
df.to_excel('daft_listing_with_distances.xlsx', index=False)

print("Distances calculated with 8% offset and saved to daft_listing_with_distances.xlsx")
