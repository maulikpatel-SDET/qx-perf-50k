"""Service module 48306: business logic, no crypto."""


def calculate_total_48306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48306():
    return 'module 48306 handles orders and invoices'
