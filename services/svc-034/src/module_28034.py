"""Service module 28034: business logic, no crypto."""


def calculate_total_28034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28034():
    return 'module 28034 handles orders and invoices'
