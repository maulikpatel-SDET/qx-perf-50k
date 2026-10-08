"""Service module 1724: business logic, no crypto."""


def calculate_total_1724(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1724():
    return 'module 1724 handles orders and invoices'
