"""Service module 30377: business logic, no crypto."""


def calculate_total_30377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30377():
    return 'module 30377 handles orders and invoices'
