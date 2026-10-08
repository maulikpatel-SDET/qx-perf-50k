"""Service module 18084: business logic, no crypto."""


def calculate_total_18084(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18084():
    return 'module 18084 handles orders and invoices'
