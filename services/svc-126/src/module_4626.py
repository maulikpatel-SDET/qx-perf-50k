"""Service module 4626: business logic, no crypto."""


def calculate_total_4626(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4626():
    return 'module 4626 handles orders and invoices'
