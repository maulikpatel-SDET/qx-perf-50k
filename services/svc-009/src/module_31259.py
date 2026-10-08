"""Service module 31259: business logic, no crypto."""


def calculate_total_31259(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31259():
    return 'module 31259 handles orders and invoices'
