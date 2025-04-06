import os
import re

def convert_spaces_to_tabs(line):
	if line.startswith("    "):
		leading_spaces = len(line) - len(line.lstrip(' '))
		tabs = '\t' * (leading_spaces // 4)
		return tabs + line.lstrip(' ')
	return line

def add_docstrings(lines):
	new_lines = []
	in_class_or_func = False
	indent = ''
	inserted_module_docstring = False

	i = 0
	while i < len(lines):
		line = lines[i]

		# Insert module-level docstring if it's not there and this is the first non-empty, non-import line
		if not inserted_module_docstring:
			if line.strip() and not line.strip().startswith(("import", "from", "#")):
				if not re.match(r'""".*?"""', line):
					new_lines.append('"""docstring"""\n\n')
				inserted_module_docstring = True

		new_lines.append(line)

		# Check for class or function
		class_match = re.match(r'^(\s*)class\s+\w+', line)
		func_match = re.match(r'^(\s*)def\s+\w+', line)

		if class_match or func_match:
			indent = class_match.group(1) if class_match else func_match.group(1)
			# Look ahead to see if next line is a docstring
			if i + 1 < len(lines):
				next_line = lines[i + 1].strip()
				if not next_line.startswith(('"""', "'''")):
					new_lines.append(f'{indent}\t"""docstring"""\n')
		i += 1

	return new_lines

def process_file(file_path):
	with open(file_path, 'r') as f:
		lines = f.readlines()

	# Convert indents
	converted = [convert_spaces_to_tabs(line) for line in lines]

	# Add docstrings
	with_docstrings = add_docstrings(converted)

	with open(file_path, 'w') as f:
		f.writelines(with_docstrings)

def process_directory(directory):
	for root, _, files in os.walk(directory):
		for file in files:
			if file.endswith(".py"):
				file_path = os.path.join(root, file)
				print(f"Processing: {file_path}")
				process_file(file_path)

if __name__ == "__main__":
	target_directory = "./bin/gainers"  # Replace this
	process_directory(target_directory)
