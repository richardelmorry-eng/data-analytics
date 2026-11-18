# Description: This script stores contact information in a dictionary
#              and prints it as a mailing address
# Author: Richard Elmorry

contact_info = {
    "name": "Alex Rivera",
    "address": "123 Main Street",
    "city": "Newark",
    "state": "NJ",
    "zip": "07102",
}

# Print the address formatted for mailing
print(f"""{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")

# Remove the name key and value
del contact_info["name"]

# Create the full_name dictionary
full_name = {"first name": "Alex", "last name": "Rivera"}

# Add an honorific to full_name with .update()
full_name.update({"honorific": "Mx."})

# Add full_name to contact_info with .update()
contact_info.update({"full_name": full_name})

# Print the address again with the new name details
print(f"""{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")