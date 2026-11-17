# Calculate van rentals for a tour group
import math

tourists = 38
seats_per_van = 15
van_cost = 250

vans_needed = math.ceil(tourists / seats_per_van)
total_cost = vans_needed * van_cost
cost_per_person = total_cost / tourists

print("Tourists: " + str(tourists))
print("Vans needed: " + str(vans_needed))
print("Total van rental cost: $" + format(total_cost, ".2f"))
print("Cost per person: $" + format(cost_per_person, ".2f"))

# Check calculations for 38 tourists:
# a) The script says to charge $19.74 per person.
# b) $19.74 x 38 = $750.12 collected.
# c) The vans cost $750.00 (3 vans x $250).
# d) There is $0.12 left over because 750 / 38 = 19.7368..., which is rounded up to $19.74 per person.