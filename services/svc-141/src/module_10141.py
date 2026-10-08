"""Service module 10141: business logic, no crypto."""


def calculate_total_10141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10141():
    return 'module 10141 handles orders and invoices'
