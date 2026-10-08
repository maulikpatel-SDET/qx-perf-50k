"""Service module 49672: business logic, no crypto."""


def calculate_total_49672(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49672():
    return 'module 49672 handles orders and invoices'
