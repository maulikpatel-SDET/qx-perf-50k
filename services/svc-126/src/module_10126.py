"""Service module 10126: business logic, no crypto."""


def calculate_total_10126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10126():
    return 'module 10126 handles orders and invoices'
