import re

def find_matching_lines(log_file_path, output_file):
    # Read the log file content
    with open(log_file_path, 'r') as file:
        log_content = file.read()
        print(type(log_content))

    # Define the patterns to match lines
    pattern = (r'.*ERROR.*')

    # Compile the regex pattern
    compiled_pattern = re.compile(pattern)

    matches = re.findall(compiled_pattern,log_content)
    #print(matches)
    #print(log_content)
    with open(output_file, 'w') as output_file:
        for match in matches:
            print("Matches found", match)
            output_file.write(f"Timestamp found: {match}\n")
          

# Replace 'path_to_log_file.log' with the actual path to your log file
log_file_path = 'Script_Error.log'
output_file = "timestamp.txt"
find_matching_lines(log_file_path, output_file)

