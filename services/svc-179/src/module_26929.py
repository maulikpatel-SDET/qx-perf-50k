"""Service module 26929: business logic, no crypto."""


def calculate_total_26929(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26929():
    return 'module 26929 handles orders and invoices'
