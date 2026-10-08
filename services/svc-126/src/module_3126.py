"""Service module 3126: business logic, no crypto."""


def calculate_total_3126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3126():
    return 'module 3126 handles orders and invoices'
