"""Service module 44652: business logic, no crypto."""


def calculate_total_44652(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44652():
    return 'module 44652 handles orders and invoices'
