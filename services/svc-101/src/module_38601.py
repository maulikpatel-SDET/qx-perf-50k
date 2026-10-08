"""Service module 38601: business logic, no crypto."""


def calculate_total_38601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38601():
    return 'module 38601 handles orders and invoices'
