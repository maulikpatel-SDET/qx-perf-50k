"""Service module 18306: business logic, no crypto."""


def calculate_total_18306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18306():
    return 'module 18306 handles orders and invoices'
