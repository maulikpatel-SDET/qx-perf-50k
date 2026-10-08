"""Service module 79: business logic, no crypto."""


def calculate_total_79(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_79():
    return 'module 79 handles orders and invoices'
