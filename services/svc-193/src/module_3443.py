"""Service module 3443: business logic, no crypto."""


def calculate_total_3443(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3443():
    return 'module 3443 handles orders and invoices'
