"""Service module 77: business logic, no crypto."""


def calculate_total_77(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_77():
    return 'module 77 handles orders and invoices'
