"""Service module 42361: business logic, no crypto."""


def calculate_total_42361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42361():
    return 'module 42361 handles orders and invoices'
