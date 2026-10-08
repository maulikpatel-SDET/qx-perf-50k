"""Service module 4431: business logic, no crypto."""


def calculate_total_4431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4431():
    return 'module 4431 handles orders and invoices'
