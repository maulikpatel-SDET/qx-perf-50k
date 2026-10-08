"""Service module 896: business logic, no crypto."""


def calculate_total_896(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_896():
    return 'module 896 handles orders and invoices'
