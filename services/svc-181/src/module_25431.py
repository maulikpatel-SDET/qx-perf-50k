"""Service module 25431: business logic, no crypto."""


def calculate_total_25431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25431():
    return 'module 25431 handles orders and invoices'
