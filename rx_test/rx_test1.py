import rx
import pprint

import time

pprint.pprint("Construct an observable:")
letters = rx.Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

disposable = rx.Observable.interval(1000) \
    .map(lambda i: "{} Mississippi".format(i)) \
    .subscribe(pprint.pprint)

time.sleep(5)

disposable.dispose()

time.sleep(5)


rx.Observable.range(1, 5).subscribe(pprint.pprint)

# Create an observable with only one item
rx.Observable.just("Hello World").subscribe(pprint.pprint)


def push_numbers(observer):
    observer.on_next(300)
    observer.on_next(500)
    observer.on_next(700)
    observer.on_completed()

pprint.pprint("Create an observable from scratch:")
rx.Observable.create(push_numbers).subscribe(pprint.pprint)


class MySubscriber(rx.Observer):

    def on_next(self, value):
        print(value)

    def on_completed(self):
        print("==== completed. ====")

    def on_error(self, error):
        print(error)


letters.subscribe(MySubscriber())

letters.subscribe(on_next=pprint.pprint,
                  on_completed=lambda: pprint.pprint("Done."))

mapped = letters.map(lambda s: len(s))

filtered = mapped.filter(lambda i: i >= 5)

filtered.subscribe(on_next=pprint.pprint,
                   on_completed=lambda: pprint.pprint("Done."))

pprint.pprint("Chained operation:")
letters.map(lambda s: len(s)) \
       .filter(lambda i: i >= 5) \
       .subscribe(pprint.pprint)





