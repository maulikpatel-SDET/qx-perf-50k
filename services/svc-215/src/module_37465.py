"""Service module 37465: business logic, no crypto."""


def calculate_total_37465(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37465():
    return 'module 37465 handles orders and invoices'
