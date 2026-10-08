"""Service module 17431: business logic, no crypto."""


def calculate_total_17431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17431():
    return 'module 17431 handles orders and invoices'
