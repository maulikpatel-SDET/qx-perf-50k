"""Service module 12287: business logic, no crypto."""


def calculate_total_12287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12287():
    return 'module 12287 handles orders and invoices'
