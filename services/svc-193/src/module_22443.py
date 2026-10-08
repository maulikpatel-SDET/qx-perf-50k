"""Service module 22443: business logic, no crypto."""


def calculate_total_22443(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22443():
    return 'module 22443 handles orders and invoices'
