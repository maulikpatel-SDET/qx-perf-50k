"""Service module 22238: business logic, no crypto."""


def calculate_total_22238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22238():
    return 'module 22238 handles orders and invoices'
