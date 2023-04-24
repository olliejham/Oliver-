print("Hello to Parents and Students of Bridgeway High School!")
print("I hope everyone is excited for the band field trip to the newly built Eight Flags Roller Coaster Park!")
print("Everyone's seats for the plane trip down are listed below:")

from collections import deque

queue_premium = deque()
queue_standard = deque()
queue_economy = deque()
packet_stream = "S Mary\nP Dee\nP Dee\nE Eileen\nE Mike\nE Joe\nP Dee\nE Vicky\nE George\nP Dee\nP Joe\nE Sally\nP Joe\nS Pete\nP Dee\nS Bill\nS Chase\nE Price\nP Dee\nE Sue"
packets = packet_stream.split('\n')
for packet in packets:
    category, name = packet.split(' ', 1)
    if category == 'P':
        queue_premium.append(name)
    elif category == 'S':
        queue_standard.append(name)
    elif category == 'E':
        queue_economy.append(name)
while queue_premium or queue_standard or queue_economy:
    if queue_premium:
        print(queue_premium.popleft())
        if queue_premium:
            print(queue_premium.popleft())
        if queue_premium:
            print(queue_premium.popleft())
    if queue_standard:
        print(queue_standard.popleft())
        if queue_standard:
            print(queue_standard.popleft())
    if queue_economy:
        print(queue_economy.popleft())
