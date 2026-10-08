"""Service module 36166: business logic, no crypto."""


def calculate_total_36166(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36166():
    return 'module 36166 handles orders and invoices'
