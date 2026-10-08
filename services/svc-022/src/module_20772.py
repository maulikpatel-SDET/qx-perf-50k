"""Service module 20772: business logic, no crypto."""


def calculate_total_20772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20772():
    return 'module 20772 handles orders and invoices'
