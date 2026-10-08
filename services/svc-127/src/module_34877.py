"""Service module 34877: business logic, no crypto."""


def calculate_total_34877(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34877():
    return 'module 34877 handles orders and invoices'
