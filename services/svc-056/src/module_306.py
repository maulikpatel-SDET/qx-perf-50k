"""Service module 306: business logic, no crypto."""


def calculate_total_306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_306():
    return 'module 306 handles orders and invoices'
