"""Service module 5126: business logic, no crypto."""


def calculate_total_5126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5126():
    return 'module 5126 handles orders and invoices'
