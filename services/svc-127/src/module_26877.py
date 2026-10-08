"""Service module 26877: business logic, no crypto."""


def calculate_total_26877(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26877():
    return 'module 26877 handles orders and invoices'
