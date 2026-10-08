"""Service module 7922: business logic, no crypto."""


def calculate_total_7922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7922():
    return 'module 7922 handles orders and invoices'
