# Importing Libraries
import csv

# Reading the `sample.log` file.
with open("sample.log", "r") as file:
    lines = file.readlines()


# 1.  Counting Requests per IP Address
ip_address_req_c = {}

for line in lines:
    ip = line.split()[0]
    if ip in ip_address_req_c:
        ip_address_req_c[ip] += 1
    else:
        ip_address_req_c[ip] = 1

# Sorting the dicgt in decreasing order
ip_address_req_c = dict(sorted(ip_address_req_c.items(), key=lambda item: item[1], reverse=True))

print(f"{'IP Address':<20}{'Request Count':<15}")
for ip, count in ip_address_req_c.items():
    print(f"{ip:<20}{count:<15}")

# Gap
print("")

# 2.  Identifying the Most Frequently Accessed Endpoint
endpoints = {}

for line in lines:
    ep = line.split()[6]
    if ep in endpoints:
        endpoints[ep] += 1
    else:
        endpoints[ep] = 1

endpoints = dict(sorted(endpoints.items(), key=lambda item: item[1], reverse=True))

# Get the first key-value pair
first_key = next(iter(endpoints))
first_value = endpoints[first_key]

print("Most Frequently Accessed Endpoint:")
print(f"{first_key} (Accessed {endpoints[first_key]} times)")

# Gap
print("")

# 3.  Detect Suspicious Activity
failed_attempts = {}

for line in lines:
    sc = line.split()[8]
    if sc == "401" or (line.split()[-2:] == ['"Invalid', 'credentials"']):
        ip = line.split()[0]
        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1

failed_attempts = dict(sorted(failed_attempts.items(), key=lambda item: item[1], reverse=True))

# Sort the dictionary by values in decreasing order
failed_attempts = sorted(failed_attempts.items(), key=lambda item: item[1], reverse=True)

# Print the header
print("Suspicious Activity Detected:")
print(f"{'IP Address':<20}{'Failed Login Attempts':<25}")

# Print each IP and its failed login count
for ip, attempts in failed_attempts:
    print(f"{ip:<20}{attempts:<25}")

# 4.  Saving to CSV
csv_file = 'log_analysis_results.csv'

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Section 1: Requests per IP
    writer.writerow(['Requests per IP'])
    writer.writerow(['IP Address', 'Request Count'])
    for ip, count in ip_address_req_c.items():
        writer.writerow([ip, count])
    writer.writerow([])  # Blank line to separate sections

    # Section 2: Most Accessed Endpoint
    writer.writerow(['Most Accessed Endpoint'])
    writer.writerow(['Endpoint', 'Access Count'])
    for endpoint, count in endpoints.items():
        writer.writerow([endpoint, count])
    writer.writerow([])  # Blank line to separate sections

    # Section 3: Suspicious Activity
    writer.writerow(['Suspicious Activity'])
    writer.writerow(['IP Address', 'Failed Login Count'])
    for ip, count in failed_attempts:
        writer.writerow([ip, count])