"""Service module 29648: business logic, no crypto."""


def calculate_total_29648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29648():
    return 'module 29648 handles orders and invoices'
