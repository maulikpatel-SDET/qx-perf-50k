"""Service module 13877: business logic, no crypto."""


def calculate_total_13877(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13877():
    return 'module 13877 handles orders and invoices'
