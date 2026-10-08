"""Service module 32033: business logic, no crypto."""


def calculate_total_32033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32033():
    return 'module 32033 handles orders and invoices'
