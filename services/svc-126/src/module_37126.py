"""Service module 37126: business logic, no crypto."""


def calculate_total_37126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37126():
    return 'module 37126 handles orders and invoices'
