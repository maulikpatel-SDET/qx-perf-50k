"""Service module 29367: business logic, no crypto."""


def calculate_total_29367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29367():
    return 'module 29367 handles orders and invoices'
