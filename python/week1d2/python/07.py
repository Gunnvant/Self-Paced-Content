import argparse
parser = argparse.ArgumentParser(description="This is where you can write the description of what the script does")
parser.add_argument("--arg1",nargs="+",help = "This is help for option --arg1")
if __name__=="__main__":
    args = parser.parse_args()
    print(args.arg1)