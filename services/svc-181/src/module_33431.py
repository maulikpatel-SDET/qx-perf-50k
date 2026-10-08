"""Service module 33431: business logic, no crypto."""


def calculate_total_33431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33431():
    return 'module 33431 handles orders and invoices'
