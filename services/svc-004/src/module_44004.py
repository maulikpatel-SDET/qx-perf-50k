"""Service module 44004: business logic, no crypto."""


def calculate_total_44004(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44004():
    return 'module 44004 handles orders and invoices'
