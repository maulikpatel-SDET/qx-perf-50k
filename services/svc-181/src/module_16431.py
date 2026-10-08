"""Service module 16431: business logic, no crypto."""


def calculate_total_16431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16431():
    return 'module 16431 handles orders and invoices'
