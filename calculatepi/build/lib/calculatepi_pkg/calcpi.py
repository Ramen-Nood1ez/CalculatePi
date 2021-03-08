"""Calculates PI to the number of iterations"""
from decimal import getcontext, Decimal
import sys
import argparse
import time
import compare_digits_of_pi as cmpi

FILE_TO_SAVE_PI_TO = "pi_test.txt"

VERSION = "0.0.7"

num_of_iter = None # pylint: disable=invalid-name

tic = None # pylint: disable=invalid-name
toc = None # pylint: disable=invalid-name

parser = argparse.ArgumentParser(description="Calculate Digits of PI.")
parser.add_argument("--iter", "-i", nargs="?", default=None,
    help="Set the amount of iterations you want to calculate pi to.")
parser.add_argument("--output", "-o", nargs="?", default=None, help="Set the file to output pi to.")
parser.add_argument("--benchmark", "-b", nargs="?", default=False, help="Sets benchmark mode on.")
parser.add_argument("--precision", "-p", nargs="?",
    default=100, help="Set the amount of precision.")
parser.add_argument("--continuefile", "-c", nargs="?", default=None,
    help="Specify the file for which you want to continue calculating pi from.")

args = parser.parse_args()

num_of_iter = args.iter if args.iter is not None else num_of_iter
FILE_TO_SAVE_PI_TO = args.output if args.output is not None else FILE_TO_SAVE_PI_TO
benchmark_mode = args.benchmark
FILE_TO_CONTINUE_TO = args.continuefile

getcontext().prec = int(args.precision) if int(args.precision) > 0 else 100

def nilakantha(reps, continue_reps=2, _pi=None, _op=None):
    """Returns PI after x amount of repetitions"""
    global num_of_iter # pylint: disable=invalid-name, global-statement
    try:
        global tic # pylint: disable=invalid-name, global-statement
        global toc # pylint: disable=invalid-name, global-statement
        tic = time.perf_counter()

        answer = Decimal(3.0) if not _pi else _pi
        op = 1 if not _op else _op # pylint: disable=invalid-name

        for n in range(continue_reps, 2 * reps + 1, 2): # pylint: disable=invalid-name
            answer += 4 / Decimal(n * (n + 1) * (n + 2) * op)
            op *= -1 # pylint: disable=invalid-name

        toc = time.perf_counter()

        return answer
    except KeyboardInterrupt:
        f = open("savedprogress.csv", "w") # pylint: disable=invalid-name, redefined-outer-name
        # File pi was saved
        f.write(f"{FILE_TO_SAVE_PI_TO},\n")
        # number of reps at
        f.write(f"{n},\n")
        # number of iterations
        f.write(f"{num_of_iter},\n")
        # op mode
        f.write(f"{op}")
        f.close()
        sys.exit()

if not benchmark_mode:
    if FILE_TO_CONTINUE_TO:
        f = open(FILE_TO_CONTINUE_TO, "r")
        file = f.read()
        f.close()
        lines = file.split(",\n")
        f = open(lines[0], "r")
        pi = Decimal(f.read())
        f.close()
        iter_to_continue_at = int(lines[1])
        num_of_iter = int(lines[2])
        op_mode = int(lines[3])

        FILE_TO_SAVE_PI_TO = lines[0]

        result = nilakantha(num_of_iter, iter_to_continue_at, pi, op_mode)
    else:
        result = nilakantha(int(num_of_iter))

    print(f"Completed calculations in: {toc - tic:0.4f} seconds")
    print(f"Or {(toc - tic) / 60} minutes")

    f = open(FILE_TO_SAVE_PI_TO, "w")
    f.write(str(result))
    f.close()

    cmpi.Main(FILE_TO_SAVE_PI_TO)
else:
    result = nilakantha(60000)

    getcontext().prec = 15

    # secondstook = (toc - tic)
    # print(secondstook)
    print(f"Benchmark completed!\nCompleted 60000 iterations in {toc - tic:0.4f} seconds")
    print(f"This computer can do about {round(60000 / (toc - tic))} iteration(s) per second")
