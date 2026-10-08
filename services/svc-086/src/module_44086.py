"""Service module 44086: business logic, no crypto."""


def calculate_total_44086(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44086():
    return 'module 44086 handles orders and invoices'
