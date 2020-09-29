from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggi']
graph['alice'] = ['peggi']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggi'] = []
graph['thom'] = []
graph['jonny'] = []

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print('No mango sellers')
    return False

print(graph)
search('you')
