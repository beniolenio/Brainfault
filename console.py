import brainfault_interpreter
import re

def main():
    print("Brainfault v1.0 console")
    print("Type \"help\" for help")
    user_cmd = None
    while user_cmd != "exit":
        user_cmd = input("Brainfault>>> ")

        # Store commands in array
        command_list = user_cmd.split(' ')

        if command_list == ['']:
            continue

        elif len(command_list) == 1:
            if command_list[0] == "brainfault":
                print("Missing argument from command...\n\nUsage:\nbrainfault [filepath/]<filename>.fault [arg1 arg2 arg3...]")
                print("ARGS ARE OPTIONAL AND MUST BE INT (e.g. 24), STRING or CHARACTER (e.g. 'str' or \"str\", 'c' or \"c\"), OR BYTE (e.g. 0b00001101)")
                print("ARGS MUST BE SEPARATED BY A SINGLE SPACE")
                print("IF FILE IS NOT IN THE CURRENT WORKING DIRECTORY, THE FULL PATH AND FILE NAME MUST BE INPUT (e.g. C:/Users/username/Documents/brainfault_file.fault)")
                continue

            elif command_list[0] == "help":
                print("Usage:\n")
                print("brainfault [filepath/]<filename>.fault [arg1 arg2 arg3...]")
                print("ARGS ARE OPTIONAL AND MUST BE INT (e.g. 24), STRING or CHARACTER (e.g. 'str' or \"str\", 'c' or \"c\"), OR BYTE (e.g. 0b00001101)")
                print("ARGS MUST BE SEPARATED BY A SINGLE SPACE")
                print("IF FILE IS NOT IN THE CURRENT WORKING DIRECTORY, THE FULL PATH AND FILE NAME MUST BE INPUT (e.g. C:/Users/username/Documents/brainfault_file.fault)")
                
                print('\n"exit" TO EXIT THE PROGRAM\n')
                continue

            elif command_list[0] != "exit":
                print("Unknown command")
                continue

        elif len(command_list) == 2 and command_list[0] == "brainfault":
            try:
                fault_file = open(command_list[1], "r")
            except FileNotFoundError:
                print(f"File or directory {command_list[1]} not found")
                continue
            brainfault_str = fault_file.read()
            fault_file.close()
            print(brainfault_interpreter.brainfault_interpreter(brainfault_str))

        elif command_list[0] == "brainfault":
            illegal_option = False
            arg_str = re.match("brainfault [^ ]+ (.+)", user_cmd).group(1)
            args = re.findall("0b[10]+|[0-9]+|'.+?'|\".+?\"", user_cmd)
            if not arg_str == ' '.join(args):
                print(arg_str, ' '.join(args))
                print("Invalid argument(s)")
                continue
            options = []
            try:
                fault_file = open(command_list[1], "r")
            except FileNotFoundError:
                print(f"File or directory {command_list[1]} not found")
                continue
            brainfault_str = fault_file.read()
            fault_file.close()
            
            for arg in args:

                if re.match("\".+\"|'.+'", arg):
                    options.extend([c for c in arg.strip("'").strip('"')])
                    continue

                if re.match("0b[01]+", arg):
                    options.append(int(arg[2:], 2))
                    continue

                if arg.isdecimal():
                    options.append(int(arg))
                    continue
                
                # No checking for invalid argument, that is done above
            print(brainfault_interpreter.brainfault_interpreter(brainfault_str, options))
        
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()