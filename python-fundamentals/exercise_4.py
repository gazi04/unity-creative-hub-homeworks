MB_PER_GB = 1024

company_name = input("Company name: ")
files_per_day = int(input("Files received per day: "))
avg_file_size_mb = int(input("Average file size (MB): "))
days = int(input("Number of days: "))
price_per_gb = float(input("Storage price per 1 GB (EUR): "))

daily_storage_mb = files_per_day * avg_file_size_mb
total_storage_mb = daily_storage_mb * days
total_storage_gb = total_storage_mb / MB_PER_GB
storage_cost = total_storage_gb * price_per_gb

print()
print("======= DATA STORAGE REPORT =======")
print(f"Company: {company_name}")
print(f"Files Per Day: {files_per_day}")
print(f"Average File Size: {avg_file_size_mb} MB")
print(f"Days: {days}")
print(f"Price per Gb: {price_per_gb}")
print()
print(f"Daily Storage: {daily_storage_mb} MB")
print(f"Total Storage: {total_storage_mb} MB")
print(f"Total Storage: {total_storage_gb:.2f} GB")
print()
print(f"Storage Cost: {storage_cost:.2f} EUR")
print("===================================")
