"""Service module 13376: business logic, no crypto."""


def calculate_total_13376(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13376():
    return 'module 13376 handles orders and invoices'
