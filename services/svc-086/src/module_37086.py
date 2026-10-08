"""Service module 37086: business logic, no crypto."""


def calculate_total_37086(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37086():
    return 'module 37086 handles orders and invoices'
