"""Service module 3922: business logic, no crypto."""


def calculate_total_3922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3922():
    return 'module 3922 handles orders and invoices'
