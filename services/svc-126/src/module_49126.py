"""Service module 49126: business logic, no crypto."""


def calculate_total_49126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49126():
    return 'module 49126 handles orders and invoices'
