"""Service module 5647: business logic, no crypto."""


def calculate_total_5647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5647():
    return 'module 5647 handles orders and invoices'
