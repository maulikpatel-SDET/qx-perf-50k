"""Service module 5877: business logic, no crypto."""


def calculate_total_5877(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5877():
    return 'module 5877 handles orders and invoices'
