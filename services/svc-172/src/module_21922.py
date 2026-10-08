"""Service module 21922: business logic, no crypto."""


def calculate_total_21922(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21922():
    return 'module 21922 handles orders and invoices'
