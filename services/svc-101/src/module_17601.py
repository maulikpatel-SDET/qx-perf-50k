"""Service module 17601: business logic, no crypto."""


def calculate_total_17601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17601():
    return 'module 17601 handles orders and invoices'
