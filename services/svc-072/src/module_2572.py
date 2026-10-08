"""Service module 2572: business logic, no crypto."""


def calculate_total_2572(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2572():
    return 'module 2572 handles orders and invoices'
