"""Service module 283: business logic, no crypto."""


def calculate_total_283(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_283():
    return 'module 283 handles orders and invoices'
