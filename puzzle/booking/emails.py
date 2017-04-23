import collections
import heapq

num = int(raw_input())

mails = collections.defaultdict(collections.deque)
all_urgency = []
max_urgent = -1
for i in range(num):
    content = raw_input().strip().split(' ')
    if content[0] == 'get_next_email':
        if not all_urgency:
            print -1
            continue
        most_urgent_indexes = mails[max_urgent]
        print most_urgent_indexes.popleft()
        if not most_urgent_indexes:
            heapq.heappop(all_urgency)
            max_urgent = -1 if not all_urgency else -all_urgency[0]
    else:
        urgent = int(content[2])
        current_urg = mails[urgent]
        if len(current_urg) == 0:
            heapq.heappush(all_urgency, -urgent)
            max_urgent = max(urgent, max_urgent)
        current_urg.append(content[1])
