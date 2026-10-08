"""Service module 29126: business logic, no crypto."""


def calculate_total_29126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29126():
    return 'module 29126 handles orders and invoices'
