"""Service module 25601: business logic, no crypto."""


def calculate_total_25601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25601():
    return 'module 25601 handles orders and invoices'
