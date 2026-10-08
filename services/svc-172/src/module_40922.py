"""Service module 40922: business logic, no crypto."""


def calculate_total_40922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40922():
    return 'module 40922 handles orders and invoices'
