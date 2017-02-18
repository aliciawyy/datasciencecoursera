import rx
from pprint import pprint

source1 = rx.Observable.from_(["Alpha", "Theta", "Beta", "Gamma", "Delta",
                               "Epsilon"])

source2 = rx.Observable.from_(["Beta", "Eta", "Theta", "Iota"])

pprint("--- merge: no order")
rx.Observable.merge(source1, source2).subscribe(pprint)

pprint("--- concatenation where order matters; an infinite line can hold the "
       "line to make the next never to be fired")
rx.Observable.concat(source1, source2).subscribe(pprint)

pprint("--- merge all")
items = ["124/12/32", "125/65/59", "236/37/85"]
rx.Observable.from_(items) \
    .map(lambda s: rx.Observable.from_(s.split("/"))) \
    .merge_all() \
    .map(int) \
    .subscribe(pprint)

pprint("--- flat map")
rx.Observable.from_(items) \
    .flat_map(lambda s: rx.Observable.from_(s.split("/"))) \
    .map(int) \
    .subscribe(pprint)

pprint("--- concat all: order matters, do not use it for infinite stream")
rx.Observable.from_(items) \
    .map(lambda s: rx.Observable.from_(s.split("/"))) \
    .concat_all() \
    .map(int) \
    .subscribe(pprint)

pprint("--- zip: stop on short one")

letters = rx.Observable.from_(list("ABCDEF"))
numbers = rx.Observable.range(1, 5)

rx.Observable.zip(letters, numbers, lambda a, b: "{}-{}".format(a, b)) \
    .subscribe(pprint)


source1 = rx.Observable.interval(1000).map(lambda i: "source 1 {}".format(i))
source2 = rx.Observable.interval(500).map(lambda i: "source 2 {}".format(i))
source3 = rx.Observable.interval(300).map(lambda i: "source 3 {}".format(i))

# rx.Observable.merge(source1, source2, source3).subscribe(pprint)

# rx.Observable.from_([source1, source2, source3]).merge_all().subscribe(pprint)


pprint("--- zip: pair finite and infinite streams")
rx.Observable.zip(letters, source1, lambda a, b: "{}-{}".format(a, b)) \
    .subscribe(pprint)

input("press any key to stop")
