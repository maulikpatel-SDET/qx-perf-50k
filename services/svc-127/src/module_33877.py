"""Service module 33877: business logic, no crypto."""


def calculate_total_33877(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33877():
    return 'module 33877 handles orders and invoices'
