"""Service module 13431: business logic, no crypto."""


def calculate_total_13431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13431():
    return 'module 13431 handles orders and invoices'
