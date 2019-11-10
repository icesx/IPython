from ftplib import print_line

from cn.i.xportal.clazz.ClassPerson import ClassPerson


def say(cp):
    print_line(cp.sayMayName())


if __name__ == '__main__':
    cp = ClassPerson("i")
    print_line(cp)
    print_line(cp.say_mine_name())
    say(cp)
    cp.set_name(" chengtao ")
    say(cp)
