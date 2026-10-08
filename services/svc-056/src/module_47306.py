"""Service module 47306: business logic, no crypto."""


def calculate_total_47306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47306():
    return 'module 47306 handles orders and invoices'
