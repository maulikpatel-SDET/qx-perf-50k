"""Service module 35126: business logic, no crypto."""


def calculate_total_35126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35126():
    return 'module 35126 handles orders and invoices'
