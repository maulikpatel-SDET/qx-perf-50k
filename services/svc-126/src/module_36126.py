"""Service module 36126: business logic, no crypto."""


def calculate_total_36126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36126():
    return 'module 36126 handles orders and invoices'
