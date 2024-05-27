# Question 3 Task 1 

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

# Iterate through the list of artist names and add them to the set
for artist in artist_names:
    unique_artists.add(artist)

# Check if duplicate playlists were found
duplicate_playlists_found = len(unique_artists) != len(artist_names)

# Output the unique artists and whether duplicate playlists were found
print(f"Unique artists: {unique_artists}")
print(f"Duplicate playlists found: {duplicate_playlists_found}")
