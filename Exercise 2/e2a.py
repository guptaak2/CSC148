# Exercise 2 (a)


class E2Error(Exception):
    pass


class E2OddError(E2Error):
    pass


def raiser(x):
        if x == "Go sue me!":
            raise E2Error("Big Apple")
        elif x != "Go sue me!":
            int(x)
            if int(x) % 2 == 0:
                raise E2OddError
            else:
                pass


