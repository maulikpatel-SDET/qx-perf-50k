"""Service module 3431: business logic, no crypto."""


def calculate_total_3431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3431():
    return 'module 3431 handles orders and invoices'
