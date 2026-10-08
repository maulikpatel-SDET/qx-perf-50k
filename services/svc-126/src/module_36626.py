"""Service module 36626: business logic, no crypto."""


def calculate_total_36626(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36626():
    return 'module 36626 handles orders and invoices'
