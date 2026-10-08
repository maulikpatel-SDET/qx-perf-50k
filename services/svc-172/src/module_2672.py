"""Service module 2672: business logic, no crypto."""


def calculate_total_2672(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2672():
    return 'module 2672 handles orders and invoices'
