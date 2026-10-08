"""Service module 6283: business logic, no crypto."""


def calculate_total_6283(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6283():
    return 'module 6283 handles orders and invoices'
