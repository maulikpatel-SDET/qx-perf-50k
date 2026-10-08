"""Service module 22283: business logic, no crypto."""


def calculate_total_22283(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22283():
    return 'module 22283 handles orders and invoices'
