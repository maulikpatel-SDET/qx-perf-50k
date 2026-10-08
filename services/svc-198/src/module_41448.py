"""Service module 41448: business logic, no crypto."""


def calculate_total_41448(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41448():
    return 'module 41448 handles orders and invoices'
