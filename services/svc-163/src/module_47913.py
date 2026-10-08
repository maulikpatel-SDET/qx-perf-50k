"""Service module 47913: business logic, no crypto."""


def calculate_total_47913(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47913():
    return 'module 47913 handles orders and invoices'
