"""Service module 16877: business logic, no crypto."""


def calculate_total_16877(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16877():
    return 'module 16877 handles orders and invoices'
