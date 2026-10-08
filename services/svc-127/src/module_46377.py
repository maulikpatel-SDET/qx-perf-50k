"""Service module 46377: business logic, no crypto."""


def calculate_total_46377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46377():
    return 'module 46377 handles orders and invoices'
