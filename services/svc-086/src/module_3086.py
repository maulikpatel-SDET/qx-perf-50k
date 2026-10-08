"""Service module 3086: business logic, no crypto."""


def calculate_total_3086(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3086():
    return 'module 3086 handles orders and invoices'
