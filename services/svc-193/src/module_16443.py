"""Service module 16443: business logic, no crypto."""


def calculate_total_16443(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16443():
    return 'module 16443 handles orders and invoices'
