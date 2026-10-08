"""Service module 21877: business logic, no crypto."""


def calculate_total_21877(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21877():
    return 'module 21877 handles orders and invoices'
