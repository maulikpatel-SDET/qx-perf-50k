"""Service module 34896: business logic, no crypto."""


def calculate_total_34896(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34896():
    return 'module 34896 handles orders and invoices'
