"""Service module 24443: business logic, no crypto."""


def calculate_total_24443(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24443():
    return 'module 24443 handles orders and invoices'
