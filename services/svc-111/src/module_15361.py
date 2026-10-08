"""Service module 15361: business logic, no crypto."""


def calculate_total_15361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15361():
    return 'module 15361 handles orders and invoices'
