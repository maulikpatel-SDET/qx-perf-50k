"""Service module 30688: business logic, no crypto."""


def calculate_total_30688(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30688():
    return 'module 30688 handles orders and invoices'
