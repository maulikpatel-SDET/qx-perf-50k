"""Service module 37283: business logic, no crypto."""


def calculate_total_37283(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37283():
    return 'module 37283 handles orders and invoices'
