import pprint

def extract_functions(filename, output_file):
    with open(filename,'r') as f:
        lines = f.readlines()
        total_blocks = []
        curr_block = []
        for line in lines:
            if "def" in line and curr_block != []:
                total_blocks.append(curr_block)
                curr_block = []
                curr_block.append(line)
            else:
                curr_block.append(line)
        total_blocks.append(curr_block)

        print("Step 1")
        pprint.pprint(total_blocks)
        print()

        parsed_total_blocks = []
        parsed_curr_blocks = []
        for func_block in total_blocks:
            are_we_finding_closing_quotes = False
            # Everything in the next for block is within one function
            for i,contents in enumerate(func_block): 
                if i == 0:
                    parsed_curr_blocks.append(contents)
                elif contents == '"""\n':
                    continue
                elif contents.find('"""') != -1 and contents.strip() != '"""':
                    # I know this lines are what I want
                    parsed_curr_blocks.append(contents)
                # This means you eitehr found opening or closing
                elif contents.strip() == '"""' and are_we_finding_closing_quotes == False:
                    are_we_finding_closing_quotes = True
                elif contents.strip() != '"""' and are_we_finding_closing_quotes == True:
                    parsed_curr_blocks.append(contents)
                elif contents.strip() == '"""' and are_we_finding_closing_quotes == True:
                    are_we_finding_closing_quotes = False
                    parsed_curr_blocks.append(contents)
            # I know the function ended
            parsed_total_blocks.append(parsed_curr_blocks)
            parsed_curr_blocks = []
        for _ in parsed_total_blocks:
            print()
            print(_)

if __name__ == "__main__":
    extract_functions("sos/python_script.py", "sos/functions.txt")