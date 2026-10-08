"""Service module 26844: business logic, no crypto."""


def calculate_total_26844(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26844():
    return 'module 26844 handles orders and invoices'
