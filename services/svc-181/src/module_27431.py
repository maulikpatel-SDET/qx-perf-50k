"""Service module 27431: business logic, no crypto."""


def calculate_total_27431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27431():
    return 'module 27431 handles orders and invoices'
