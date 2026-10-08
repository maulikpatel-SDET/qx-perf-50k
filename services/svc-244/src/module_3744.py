"""Service module 3744: business logic, no crypto."""


def calculate_total_3744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3744():
    return 'module 3744 handles orders and invoices'
