"""Service module 42922: business logic, no crypto."""


def calculate_total_42922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42922():
    return 'module 42922 handles orders and invoices'
