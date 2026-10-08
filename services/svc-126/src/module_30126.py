"""Service module 30126: business logic, no crypto."""


def calculate_total_30126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30126():
    return 'module 30126 handles orders and invoices'
