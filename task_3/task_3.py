import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

cities = [
    "Kyiv",
    "Lviv",
    "Odessa",
    "Kharkiv",
    "Dnipro",
    "Zaporizhzhia",
    "Mykolaiv",
    "Vinnytsia",
    "Ivano-Frankivsk",
    "Ternopil",
    "Lutsk",
    "Cherkasy",
    "Chernihiv",
    "Sumy",
    "Rivne",
    "Zhytomyr",
    "Poltava",
    "Uzhhorod",
    "Chernivtsi",
    "Kropyvnytskyi",
]

G.add_nodes_from(cities)

# Додаємо ребра (шляхи між містами) з вагами
# (відстані між містами в кілометрах)
edges_with_weights = [
    ("Kyiv", "Lviv", 540),
    ("Kyiv", "Odessa", 480),
    ("Kyiv", "Kharkiv", 470),
    ("Kyiv", "Dnipro", 450),
    ("Kyiv", "Chernihiv", 140),
    ("Kyiv", "Zhytomyr", 130),
    ("Lviv", "Ternopil", 130),
    ("Lviv", "Ivano-Frankivsk", 130),
    ("Lviv", "Lutsk", 150),
    ("Odessa", "Mykolaiv", 130),
    ("Odessa", "Dnipro", 480),
    ("Dnipro", "Zaporizhzhia", 80),
    ("Dnipro", "Kharkiv", 215),
    ("Zaporizhzhia", "Mykolaiv", 300),
    ("Cherkasy", "Vinnytsia", 260),
    ("Vinnytsia", "Zhytomyr", 120),
    ("Zhytomyr", "Rivne", 190),
    ("Rivne", "Lutsk", 70),
    ("Sumy", "Chernihiv", 180),
    ("Kharkiv", "Poltava", 140),
    ("Chernivtsi", "Ivano-Frankivsk", 140),
    ("Chernivtsi", "Ternopil", 190),
    ("Uzhhorod", "Lviv", 260),
    ("Kropyvnytskyi", "Mykolaiv", 210),
]

# Додаємо ребра з вагами до графа
G.add_weighted_edges_from(edges_with_weights)

# Візуалізуємо граф із вагами ребер
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=1000,
    font_size=10,
    edge_color="gray",
    font_weight="bold",
)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Transport Network of Ukraine (with Weights)")
plt.show()


# Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів
def dijkstra_all_paths(graph, start_node):
    return nx.single_source_dijkstra_path_length(graph, start_node)


# Вибираємо стартове місто
start_city = "Kyiv"

# Знаходимо найкоротші шляхи від стартового міста до всіх інших міст
shortest_paths = dijkstra_all_paths(G, start_city)

# Виводимо найкоротші шляхи
print(f"Найкоротші шляхи від {start_city}:")
for city, distance in shortest_paths.items():
    print(f"Від {start_city} до {city}: {distance} км")
