import os, csv

def get_data(data_path):
	# Gets correct data path, platform independent
	data_path = [path.replace('/', os.sep) for path in data_path]
	if os.path.exists(data_path[0]):
		data_path = data_path[0]
	else:
		data_path = data_path[1]

	# Opens csv and reads data to dict via dict comprehension
	data_dict = {}
	with open(data_path) as cf:
		data_dict = {
			month.strip() : int(val.strip()) for month, val in csv.reader(cf)
		}

	return data_dict, data_path

def print_monthly(data_dict):
	# Prints month and val from data dict
	for month, val in data_dict.items():
		print(f'{month} - {val}')
	print()

def print_yearly(data_dict):
	# Gets list of values, sum, rounded avg, then prints
	val_list = list(data_dict.values())
	total = sum(val_list)
	avg = round(total / len(val_list), 2)
	print(f'Yearly total:     {total}')
	print(f'Monthly average:  {avg}\n')

def edit_data(data_dict, data_path):
	# Get valid months and user month
	month_list = list(data_dict.keys())
	month = input('Three-letter Month: ').strip()
	
	# If month is valid, else error
	if month in month_list:
		# Gets new val from user and saves to dict
		val = int(input('Sales Amount: ').strip())
		data_dict[month] = val

		# Saves data to csv file we opened earlier
		save_data(data_dict, data_path)
		print(f'Sales amount for {month} was modified.\n')

	else:
		# Entered invalid month
		print('Invalid three-letter month.\n')

def save_data(data_dict, data_path):
	# Saves updated data dict to csv file we opened
	with open(data_path, 'w') as cf:
		writer = csv.writer(cf)
		for item in data_dict.items():
			writer.writerows([item])

def main():
	# CSV data path, works both in and just outside program directory.
	data_path = ['../data/monthly_sales.csv', 'data/monthly_sales.csv']

	# Read data from csv
	data_dict, data_path = get_data(data_path)
	
	# Print program title and commands
	print('Monthly Sales program\n')
	print('COMMAND MENU')
	print('monthly - View monthly sales')
	print('yearly  - View yearly summary')
	print('edit    - Edit sales for a month')
	print('exit    - Exit program\n')

	# Gets command and runs until exit
	cont_flag = True
	while cont_flag:
		# Gets user command
		cmd = input('Command: ').strip()

		# Prints monthly
		if cmd == 'monthly':
			print_monthly(data_dict)

		# Prints yearly
		elif cmd == 'yearly':
			print_yearly(data_dict)

		# Edits and saves data
		elif cmd == 'edit':
			edit_data(data_dict, data_path)

		# Exits program
		elif cmd == 'exit':
			print('Bye!')
			cont_flag = False

		# Invalid command entry
		else:
			# Didnt say to print cmd error but if you did thats fine
			print()

if __name__ == '__main__':
	main()