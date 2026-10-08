"""Service module 30922: business logic, no crypto."""


def calculate_total_30922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30922():
    return 'module 30922 handles orders and invoices'
