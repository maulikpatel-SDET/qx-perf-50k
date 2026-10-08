"""Service module 40688: business logic, no crypto."""


def calculate_total_40688(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40688():
    return 'module 40688 handles orders and invoices'
