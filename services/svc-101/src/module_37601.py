"""Service module 37601: business logic, no crypto."""


def calculate_total_37601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37601():
    return 'module 37601 handles orders and invoices'
