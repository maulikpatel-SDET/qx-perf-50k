"""Service module 26443: business logic, no crypto."""


def calculate_total_26443(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26443():
    return 'module 26443 handles orders and invoices'
