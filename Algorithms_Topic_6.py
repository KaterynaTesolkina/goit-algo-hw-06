# Завдання 1:
import networkx as nx
import matplotlib.pyplot as plt
# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (комп'ютери)
G.add_nodes_from(['Комп\'ютер 1', 'Комп\'ютер 2', 'Комп\'ютер 3', 'Роутер 1', 'Роутер 2'])

# Додавання ребер (з'єднання)
G.add_edges_from([('Комп\'ютер 1', 'Роутер 1'), ('Комп\'ютер 2', 'Роутер 1'),
                  ('Комп\'ютер 3', 'Роутер 2'), ('Роутер 1', 'Роутер 2')])

# Візуалізація графа
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold')
plt.title("Інтернет-топологія")
plt.show()
# Основні характеристики графа
print("Кількість вершин (комп'ютерів та роутерів):", G.number_of_nodes())
print("Кількість ребер (з'єднань):", G.number_of_edges())

# Ступінь вершин (кількість з'єднань для кожної вершини)
print("Ступінь вершин (кількість з'єднань для кожної вершини):")
degrees = dict(G.degree())
for node, degree in degrees.items():
    print(f"{node}: {degree}")

# Завдання 2:

import networkx as nx

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for next_node in graph[node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)

# Наш граф
G = nx.Graph()
G.add_nodes_from(['Комп\'ютер 1', 'Комп\'ютер 2', 'Комп\'ютер 3', 'Роутер 1', 'Роутер 2'])
G.add_edges_from([('Комп\'ютер 1', 'Роутер 1'), ('Комп\'ютер 2', 'Роутер 1'),
                  ('Комп\'ютер 3', 'Роутер 2'), ('Роутер 1', 'Роутер 2')])

# Виклик алгоритмів DFS і BFS
print("DFS:")
dfs(dict(G.adjacency()), 'Комп\'ютер 1')
print("\nBFS:")
bfs(dict(G.adjacency()), 'Комп\'ютер 1')

# Завдання 3:

import networkx as nx

def dijkstra(graph, start):
    # Ініціалізація відстаней
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Створення списку відвіданих вершин
    visited = set()
    
    # Головний цикл алгоритму
    while len(visited) < len(graph):
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None:
                    min_node = node
                elif distances[node] < distances[min_node]:
                    min_node = node
        
        # Позначення вершини як відвіданої
        visited.add(min_node)
        
        # Оновлення відстаней до сусідніх вершин через поточну вершину
        for neighbor, edge_data in graph[min_node].items():
            weight = edge_data['weight']  # Отримуємо вагу ребра
            if distances[min_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_node] + weight
    
    return distances

# Створення графа з вагами ребер
G = nx.Graph()
G.add_nodes_from(['Комп\'ютер 1', 'Комп\'ютер 2', 'Комп\'ютер 3', 'Роутер 1', 'Роутер 2'])
G.add_weighted_edges_from([('Комп\'ютер 1', 'Роутер 1', {'weight': 3}), ('Комп\'ютер 2', 'Роутер 1', {'weight': 5}),
                           ('Комп\'ютер 3', 'Роутер 2', {'weight': 2}), ('Роутер 1', 'Роутер 2', {'weight': 1})])

# Визначення найкоротших шляхів від вершини 'Комп\'ютер 1'
shortest_paths = dijkstra(G, 'Комп\'ютер 1')
print("Найкоротші шляхи від вершини 'Комп\'ютер 1':")
for node, distance in shortest_paths.items():
    print(f"{node}: {distance}")
