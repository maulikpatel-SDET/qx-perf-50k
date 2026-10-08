"""Service module 31431: business logic, no crypto."""


def calculate_total_31431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31431():
    return 'module 31431 handles orders and invoices'
