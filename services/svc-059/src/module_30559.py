"""Service module 30559: business logic, no crypto."""


def calculate_total_30559(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30559():
    return 'module 30559 handles orders and invoices'
