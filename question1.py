# Question 1 Task 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
print(f"Destinations both airlines fly to: {common_destinations}")

unique_destinations = our_routes.difference(competitor_routes)
print(f"Destinations unique to our airline: {unique_destinations}")

neither_share = our_routes.isdisjoint(competitor_routes)
print(f"Are there any destinations that neither airline shares? {'Yes' if neither_share else 'No'}")
