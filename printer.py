__author__ = 'PLNech'

# noinspection PyClassHasNoInit
class Printer:
    HEADER = '\033[95m'
    END = '\033[0m'

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    BOLD = "\033[1m"

    @staticmethod
    def disable():
        Printer.HEADER = ''
        Printer.BLUE = ''
        Printer.GREEN = ''
        Printer.WARNING = ''
        Printer.FAIL = ''
        Printer.END = ''

    @staticmethod
    def green(msg):
        return Printer.color(msg, Printer.GREEN)

    @staticmethod
    def blue(msg):
        return Printer.color(msg, Printer.BLUE)

    @staticmethod
    def red(msg):
        return Printer.color(msg, Printer.RED)

    @staticmethod
    def bold(msg):
        return Printer.color(msg, Printer.BOLD)

    @staticmethod
    def color(msg, color):
        return str(color) + str(msg) + str(Printer.END)

    @staticmethod
    def info(msg):
        colored_msg = Printer.blue(msg)
        # print(colored_msg)
        return colored_msg

    @staticmethod
    def warn(msg):
        colored_msg = Printer.WARNING + msg + Printer.END
        print(colored_msg)
        return colored_msg

    @staticmethod
    def err(msg):
        colored_msg = Printer.red(msg)
        print(colored_msg)
        return colored_msg

    @staticmethod
    def fail():
        return Printer.err("FAIL")

    @staticmethod
    def ok():
        return Printer.green("OK")

    @staticmethod
    def if_bigger(msg, v1, v2):
        if v1 == v2:
            return Printer.bold(msg)
        elif v1 < v2 or float(v1) < float(v2) or int(v1 < int(v2)):
            return Printer.red(msg)
        else:
            return Printer.green(msg)

    @staticmethod
    def if_positive(msg, value):
        if value == 0:
            return Printer.bold(msg)
        elif value < 0:
            return Printer.red(msg)
        else:
            return Printer.green(msg)

    @staticmethod
    def print_diff(str1, str2, ignore_chars="-> "):
        len1, len2 = len(str1), len(str2)
        try:
            assert (len1 == len2)
        except AssertionError:
            print("The given strings are of different lengths: _%s_/_%s_ (%d/%d)." % (str1, str2, len1, len2))
            raise

        list_str = ""
        for c1, c2 in zip(str1, str2):
            if c1 in ignore_chars:
                list_str = list_str + c1
            elif c1 == c2:
                list_str += Printer.green(c1)
            else:
                list_str += Printer.red(c2)
        return list_str

    @staticmethod
    def print_and_log(message, f):
        """

        :param message: The message to process
        :type message str
        :param f: The file descriptor of the file
        :type f file
        """
        print(message)
        f.write(message + "\n")
