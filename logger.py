import inspect


class bcolors:
    INFO = '\033[95m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'


levels = ["INFO", "SUCCESS", "WARNING", "ERROR"]

# gets the line of the file that you call it from


def getLine():
    return inspect.getframeinfo(inspect.stack()[3][0]).lineno

# gets the path of the file that you call it from


def getPath():
    return inspect.getframeinfo(inspect.stack()[3][0]).filename

# concats the message so you can have as many as you want


def concatMessage(message, level):
    toReturn = f'{getPath()}:{str(getLine())}:{levels[level]}: '
    for lines in message:
        toReturn += str(lines) + " "
    return toReturn


def info(*message):
    message = concatMessage(message, 0)
    print(bcolors.INFO + message + bcolors.ENDC, flush=True)


def success(*message):
    message = concatMessage(message, 1)
    print(bcolors.SUCCESS + message + bcolors.ENDC, flush=True)


def warning(*message):
    message = concatMessage(message, 2)
    print(bcolors.WARNING + message + bcolors.ENDC, flush=True)


def error(*message):
    message = concatMessage(message, 3)
    print(bcolors.ERROR + message + bcolors.ENDC, flush=True)
