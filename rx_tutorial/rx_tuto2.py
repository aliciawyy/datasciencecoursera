import rx
from pprint import pprint

numbers = rx.Observable.from_([2, 5, 21, 5, 2, 1, 127, 63])

numbers.take_while(lambda i: i < 127).subscribe(pprint)

pprint("distinct")
numbers.distinct().subscribe(pprint)

letters = rx.Observable.from_(["Alpha", "Theta", "Beta", "Gamma", "Delta",
                               "Epsilon"])
letters.distinct(len).subscribe(pprint)

pprint("--- distinct_until_changed")
letters.distinct_until_changed(len).subscribe(pprint)

pprint("--- count")
letters.filter(lambda s: len(s) != 5).count().subscribe(pprint)

pprint("--- reduce")
numbers.filter(lambda p: p < 60).sum().subscribe(pprint)
numbers.filter(lambda p: p < 60).reduce(lambda total, i: total + i) \
    .subscribe(pprint)

pprint("--- scan: makes rolling aggregation")
numbers.filter(lambda p: p < 60).scan(lambda total, i: total + i) \
    .subscribe(pprint)

pprint("--- collect: it runs after on_completed")
letters.to_list().subscribe(pprint)
letters.to_dict(lambda p: p[0]).subscribe(pprint)
# second argument is value
letters.to_dict(lambda p: p[0], lambda p: len(p)).subscribe(pprint)


pprint("--- group by")
source1 = rx.Observable.from_(["Alpha", "Theta", "Beta", "Gamma", "Delta",
                               "Epsilon"])

source1.group_by(lambda p: len(p))\
    .flat_map(lambda g: g.to_list()) \
    .subscribe(pprint)

source1.group_by(lambda p: len(p))\
    .flat_map(lambda g: g.count().map(lambda cnt: (g.key, cnt))) \
    .subscribe(pprint)
