"""Service module 12160: business logic, no crypto."""


def calculate_total_12160(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12160():
    return 'module 12160 handles orders and invoices'
