"""Service module 82: business logic, no crypto."""


def calculate_total_82(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_82():
    return 'module 82 handles orders and invoices'
