"""Service module 2283: business logic, no crypto."""


def calculate_total_2283(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2283():
    return 'module 2283 handles orders and invoices'
