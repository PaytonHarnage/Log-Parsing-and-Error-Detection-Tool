import re

def read_log_file(file_path):
    """Reads a log file and returns its contents as a list of lines."""
    try:
        with open(file_path, 'r') as file:
            log_content = file.readlines()
        return log_content
    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return None

def parse_log_for_errors(log_lines):
    """Parse the log lines and extract errors or warnings."""
    error_patterns = [
        r"ERROR",        # Match lines containing "ERROR"
        r"WARNING",      # Match lines containing "WARNING"
        r"\[CRITICAL\]", # Match lines containing "[CRITICAL]"
    ]
    
    errors = []
    
    # Loop through each line in the log content and search for error patterns
    for line in log_lines:
        for pattern in error_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                errors.append(line.strip())
                
    return errors

def generate_error_report(errors):
    """Generate a report of the detected errors."""
    if not errors:
        return "No errors or warnings found in the log file."

    report = "Error Report:\n"
    report += "=" * 50 + "\n"
    
    for i, error in enumerate(errors, start=1):
        report += f"{i}. {error}\n"
    
    return report

def main():
    # Path to your log file (you can change the path to your own log file)
    file_path = "sample_log.txt"
    
    # Read the log file
    log_lines = read_log_file(file_path)
    
    if log_lines:
        # Parse the log file for errors
        errors = parse_log_for_errors(log_lines)
        
        # Generate the error report
        report = generate_error_report(errors)
        
        # Print the report to the console
        print(report)

if __name__ == "__main__":
    main()
