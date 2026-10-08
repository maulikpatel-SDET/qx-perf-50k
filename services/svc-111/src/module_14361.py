"""Service module 14361: business logic, no crypto."""


def calculate_total_14361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14361():
    return 'module 14361 handles orders and invoices'
