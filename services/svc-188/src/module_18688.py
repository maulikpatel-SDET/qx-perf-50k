"""Service module 18688: business logic, no crypto."""


def calculate_total_18688(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18688():
    return 'module 18688 handles orders and invoices'
