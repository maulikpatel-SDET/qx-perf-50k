"""Service module 7918: business logic, no crypto."""


def calculate_total_7918(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7918():
    return 'module 7918 handles orders and invoices'
