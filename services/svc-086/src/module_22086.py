"""Service module 22086: business logic, no crypto."""


def calculate_total_22086(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22086():
    return 'module 22086 handles orders and invoices'
