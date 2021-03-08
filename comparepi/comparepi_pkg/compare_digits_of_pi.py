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
        correct_pi_str = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989
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
