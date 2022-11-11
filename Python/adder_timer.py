from argparse import ArgumentParser
from time import sleep

parser = ArgumentParser()
parser.add_argument("time", type = int)
args = parser.parse_args()

print(f"Starting timer of {args.time} seconds")

total_sum = 0
for i in range(args.time):
    total_sum += i
    print(total_sum, end = " ", flush = True)
    sleep(1)

print("\nDone!!")