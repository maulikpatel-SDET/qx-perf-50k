"""Service module 1601: business logic, no crypto."""


def calculate_total_1601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1601():
    return 'module 1601 handles orders and invoices'
