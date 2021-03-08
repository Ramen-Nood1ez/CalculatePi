"""Compares the given file to the correct pi file"""
CORRECT_PI_FILE = "digits_of_pi.txt"
class Main: # pylint: disable=too-few-public-methods
    """Compares the given file to the correct pi file"""
    def __init__(self, compare_file=None):
        if compare_file is None:
            self.compare_file = input("Enter in the location of the "
                                     + "file you want to compare pi to\n> ")
        else:
            self.compare_file = compare_file

        self.show_arrow = ""

        self.compare()

    def compare(self):
        """Compares the given file to the correct pi file"""
        correct_pi = open(CORRECT_PI_FILE, "r")
        correct_pi_str = correct_pi.read()
        # print(correct_pi.read())

        compare_pi = open(self.compare_file, "r")
        compare_pi_str = compare_pi.read()
        # print(compare_pi.read())

        for i in enumerate(compare_pi_str):
            if compare_pi_str[i[0]] != correct_pi_str[i[0]]:
                print(f"Value incorrect at number: {i[0] + 1}"
                     + f"({compare_pi_str[i[0]]} instead of {correct_pi_str[i[0]]})")
                self.show_arrow += "^"
            else:
                self.show_arrow += " "
                continue

        print(f"Here are the incorrect values:\n{compare_pi_str}\n{self.show_arrow}")

        correct_values_up_to = ""

        for k in range(len(compare_pi_str)):
            correct_values_up_to += correct_pi_str[k]

        print(f"\nHere are the correct values:\n{correct_values_up_to}\n{self.show_arrow}")
