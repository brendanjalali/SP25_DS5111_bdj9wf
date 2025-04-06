import os

def convert_spaces_to_tabs(file_path):
	with open(file_path, 'r') as f:
		lines = f.readlines()

	# Replace 4 leading spaces with a tab on each line
	converted_lines = []
	for line in lines:
		new_line = line
		if line.startswith("    "):  # Only replace leading indents
			leading_spaces = len(line) - len(line.lstrip(' '))
			tabs = '\t' * (leading_spaces // 4)
			new_line = tabs + line.lstrip(' ')
		converted_lines.append(new_line)

	with open(file_path, 'w') as f:
		f.writelines(converted_lines)

def process_directory(directory):
	for root, _, files in os.walk(directory):
		for file in files:
			if file.endswith(".py"):
				file_path = os.path.join(root, file)
				print(f"Converting: {file_path}")
				convert_spaces_to_tabs(file_path)

if __name__ == "__main__":
	target_directory = "./bin/gainers"  # Replace with your target directory
	process_directory(target_directory)
