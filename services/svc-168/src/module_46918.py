"""Service module 46918: business logic, no crypto."""


def calculate_total_46918(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46918():
    return 'module 46918 handles orders and invoices'
