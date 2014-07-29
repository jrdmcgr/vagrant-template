import sys
import time


def status_bar(numerator, denominator, chars='[=>_]'):
    start, complete, head, incomplete, end = chars
    incomplete *= (denominator - numerator)
    complete *= numerator
    sys.stdout.write(start + complete + head + incomplete + end + '\r')
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(51):
        status_bar(i, 50)
        time.sleep(0.2)
    sys.stdout.write('\n')
