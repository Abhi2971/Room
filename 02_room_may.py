# 1apr to 30 apr

# Rent and bill amounts
R_rent = 8000
l_bill = 3306
G_bill = 0

# Initial dictionary with members and their respective shares
may_dict = {
    "Abhi": 0,
    "Ganesh": 0,
    "Hemant": 0,
    "Sunil": 0,
    "Kiran": 0,
    "KB": 0
}

# Number of members
num_members = len(may_dict)
num_full_members = num_members - 1  # KB is not a full member

# Split the rent and electricity bill equally among all members
for key in may_dict:
    if key == "KB":
        may_dict[key] = (R_rent / num_members + l_bill / num_members) / 2
    else:
        may_dict[key] = R_rent / num_members + l_bill / num_members

# Split the gas bill among 4 members (excluding Kiran and KB)
for key in may_dict:
    if key not in ["Kiran", "KB"]:
        may_dict[key] += G_bill / 4

# Calculate the remaining amount that needs to be added to full members due to KB paying half
remaining_amount = (R_rent / num_members + l_bill / num_members) / 2

# Add the remaining amount to each full member
for key in may_dict:
    if key != "KB":
        may_dict[key] += remaining_amount / num_full_members

print("May dictionary with KB half month and gas bill split:")
print(may_dict)

# Verifying the total amounts
total_rent_light = R_rent + l_bill
total_gas = G_bill
total_additional = remaining_amount

total_shared = sum(may_dict.values())
expected_total = total_rent_light + total_gas

print(f"Total shared: {total_shared}")
print(f"Expected total: {expected_total}")
