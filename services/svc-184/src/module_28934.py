"""Service module 28934: business logic, no crypto."""


def calculate_total_28934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28934():
    return 'module 28934 handles orders and invoices'
