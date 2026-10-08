"""Service module 44377: business logic, no crypto."""


def calculate_total_44377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44377():
    return 'module 44377 handles orders and invoices'
