"""Service module 8450: business logic, no crypto."""


def calculate_total_8450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8450():
    return 'module 8450 handles orders and invoices'
