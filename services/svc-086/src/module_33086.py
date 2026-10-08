"""Service module 33086: business logic, no crypto."""


def calculate_total_33086(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33086():
    return 'module 33086 handles orders and invoices'
