"""Service module 13626: business logic, no crypto."""


def calculate_total_13626(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13626():
    return 'module 13626 handles orders and invoices'
