import compare_digits_of_pi as cmpi
import keyboard
import threading, queue
import time
import argparse
import numpy as np

q = queue.Queue()

pi = np.longdouble(3)
adding_mode = True
third_digit = np.int64(4)
quitdigits = False
tic = None
toc = None
benchmark_mode = False

COMPARE_AT_END = True
DEFAULT_ITERATIONS = 30000
#DEFAULT_ITERATIONS = 10000
TIME_DELAY = 0
STORED_DELAY = 0.5

FILE_TO_SAVE_PI_TO = "pi_test.txt"

numofiter = None

parser = argparse.ArgumentParser(description="Calculate Digits of PI.")
parser.add_argument("--iter", "-i", nargs="?", default=None,
    help="Set the amount of iterations you want to calculate pi to.")
parser.add_argument("--output", "-o", nargs="?", default=None, help="Set the file to output pi to.")
parser.add_argument("--benchmark", "-b", nargs="?", default=False, help="Sets benchmark mode on")

args = parser.parse_args()

numofiter = args.iter if args.iter != None else numofiter
FILE_TO_SAVE_PI_TO = args.output if args.output != None else FILE_TO_SAVE_PI_TO
benchmark_mode = args.benchmark

if benchmark_mode:
    numofiter = 60000

userinput = input("How many iterations do you want to calculate for pi?\n> ") if numofiter == None else numofiter

i = 1

keyboard.on_press_key("q", lambda _:set_quit_digits())
keyboard.on_press_key("s", lambda _:set_using_time_delay())

def set_quit_digits():
    global quitdigits
    global pi
    quitdigits = True

    for i in range(len(q.queue)):
        q.task_done()

def set_using_time_delay():
    global TIME_DELAY
    global STORED_DELAY

    if TIME_DELAY == 0:
        TIME_DELAY = STORED_DELAY
    else:
        STORED_DELAY = TIME_DELAY
        TIME_DELAY = 0

def worker():
    global userinput
    global adding_mode
    global pi
    global quitdigits
    global third_digit
    global i
    global tic
    global toc

    tic = time.perf_counter()

    if userinput == "" or int(userinput) == 0 or int(userinput) < -1:
        userinput = DEFAULT_ITERATIONS

    if int(userinput) > 0:
        while i < int(userinput):

            time.sleep(TIME_DELAY)

            item = q.get()

            print(f"Item: {item}")

            if quitdigits: break

            if adding_mode:
                # pi += 4 / ((third_digit - 2) * (third_digit - 1) * third_digit)
                pi += np.longdouble(4 / ((item - 2) * (item - 1) * item))
            else:
                # pi -= 4 / ((third_digit - 2) * (third_digit - 1) * third_digit)
                pi -= np.longdouble(4 / ((item - 2) * (item - 1) * item))
            
            adding_mode = not adding_mode
            # third_digit += 2
            print(f"{i + 1}:\n{pi}")
            i += 1

            if quitdigits: break
            q.task_done()
    else:
        while True:

            time.sleep(TIME_DELAY)

            item = q.get()

            if quitdigits: break

            if adding_mode:
                # pi += 4 / ((third_digit - 2) * (third_digit - 1) * third_digit)
                pi += np.longdouble(4 / ((item - 2) * (item - 1) * item))
            else:
                # pi -= 4 / ((third_digit - 2) * (third_digit - 1) * third_digit)
                pi -= np.longdouble(4 / ((item - 2) * (item - 1) * item))
            
            adding_mode = not adding_mode
            third_digit += 2
            print(f"{i + 1}:\n{pi}")
            i += 1

            if quitdigits: break
            q.task_done()
            q.put(third_digit)

    q.task_done()
    toc = time.perf_counter()

threading.Thread(target=worker, daemon=True).start()

third_digit_copy = third_digit

for k in range(int(userinput)):
    q.put(third_digit)
    third_digit += 2

if int(userinput) == -1:
    q.put(third_digit)

third_digit = third_digit_copy
del third_digit_copy

q.join()

if not benchmark_mode:
    print(f"Completed calculations in: {toc - tic:0.4f} seconds")

    f = open(FILE_TO_SAVE_PI_TO, "w")
    f.write(str(pi))
    f.close()

    if COMPARE_AT_END:
        compare_pi = cmpi.Main(FILE_TO_SAVE_PI_TO)
else:
    secondstook = (toc - tic)
    print(secondstook)
    print(f"Benchmark completed!\nCompleted 60000 iterations in {toc - tic:0.4f} seconds")
    print(f"This computer can do about {round(60000 / (toc - tic))} iteration(s) per second")