import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
G = nx.Graph()

# Додаємо міста як вершини
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

# Додаємо транспортні зв'язки між містами
edges = [
    ("Kyiv", "Lviv"),
    ("Kyiv", "Odessa"),
    ("Kyiv", "Kharkiv"),
    ("Kyiv", "Dnipro"),
    ("Kyiv", "Chernihiv"),
    ("Kyiv", "Zhytomyr"),
    ("Lviv", "Ternopil"),
    ("Lviv", "Ivano-Frankivsk"),
    ("Lviv", "Lutsk"),
    ("Odessa", "Mykolaiv"),
    ("Odessa", "Dnipro"),
    ("Dnipro", "Zaporizhzhia"),
    ("Dnipro", "Kharkiv"),
    ("Zaporizhzhia", "Mykolaiv"),
    ("Cherkasy", "Vinnytsia"),
    ("Vinnytsia", "Zhytomyr"),
    ("Zhytomyr", "Rivne"),
    ("Rivne", "Lutsk"),
    ("Sumy", "Chernihiv"),
    ("Kharkiv", "Poltava"),
    ("Chernivtsi", "Ivano-Frankivsk"),
    ("Chernivtsi", "Ternopil"),
    ("Uzhhorod", "Lviv"),
    ("Kropyvnytskyi", "Mykolaiv"),
]

G.add_edges_from(edges)

# Візуалізуємо граф
plt.figure(figsize=(12, 10))
nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    font_weight="bold",
    node_size=1000,
    font_size=10,
    edge_color="gray",
)
plt.title("Transport Network of Ukraine (Cities)")
plt.show()

# Аналіз характеристик графа
print(f"Кількість міст (вершин): {G.number_of_nodes()}")
print(f"Кількість шляхів (ребер): {G.number_of_edges()}")
print(f"Ступінь кожного міста: {dict(G.degree())}")
