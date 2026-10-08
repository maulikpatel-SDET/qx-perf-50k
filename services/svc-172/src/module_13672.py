"""Service module 13672: business logic, no crypto."""


def calculate_total_13672(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13672():
    return 'module 13672 handles orders and invoices'
