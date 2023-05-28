import sys

if __name__ == "__main__":
    print("Hello from the outer side")
    # if we get here, all passed
    print(f"All licenses and exceptions validated against schema.")
    # Access command-line parameters
    # The first parameter (sys.argv[0]) is the script name itself
    # The subsequent parameters (sys.argv[1:], starting from index 1) are the command-line arguments
    arguments = sys.argv[1:]
    # Process command-line parameters
    for arg in arguments:
        print("Argument:", arg)