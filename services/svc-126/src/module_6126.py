"""Service module 6126: business logic, no crypto."""


def calculate_total_6126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6126():
    return 'module 6126 handles orders and invoices'
