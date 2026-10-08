"""Service module 23922: business logic, no crypto."""


def calculate_total_23922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23922():
    return 'module 23922 handles orders and invoices'
