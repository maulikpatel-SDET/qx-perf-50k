"""Service module 17922: business logic, no crypto."""


def calculate_total_17922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17922():
    return 'module 17922 handles orders and invoices'
