"""Service module 3672: business logic, no crypto."""


def calculate_total_3672(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3672():
    return 'module 3672 handles orders and invoices'
