"""Service module 1361: business logic, no crypto."""


def calculate_total_1361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1361():
    return 'module 1361 handles orders and invoices'
