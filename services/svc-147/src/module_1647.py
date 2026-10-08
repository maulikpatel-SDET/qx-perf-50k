"""Service module 1647: business logic, no crypto."""


def calculate_total_1647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1647():
    return 'module 1647 handles orders and invoices'
