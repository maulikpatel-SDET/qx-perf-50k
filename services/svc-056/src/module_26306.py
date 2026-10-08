"""Service module 26306: business logic, no crypto."""


def calculate_total_26306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26306():
    return 'module 26306 handles orders and invoices'
