"""Service module 39922: business logic, no crypto."""


def calculate_total_39922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39922():
    return 'module 39922 handles orders and invoices'
