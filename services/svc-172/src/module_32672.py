"""Service module 32672: business logic, no crypto."""


def calculate_total_32672(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32672():
    return 'module 32672 handles orders and invoices'
