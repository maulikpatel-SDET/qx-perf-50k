"""Service module 41922: business logic, no crypto."""


def calculate_total_41922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41922():
    return 'module 41922 handles orders and invoices'
