"""Service module 2744: business logic, no crypto."""


def calculate_total_2744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2744():
    return 'module 2744 handles orders and invoices'
