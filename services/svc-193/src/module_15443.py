"""Service module 15443: business logic, no crypto."""


def calculate_total_15443(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15443():
    return 'module 15443 handles orders and invoices'
