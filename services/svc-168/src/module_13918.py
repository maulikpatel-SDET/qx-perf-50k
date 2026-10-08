"""Service module 13918: business logic, no crypto."""


def calculate_total_13918(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13918():
    return 'module 13918 handles orders and invoices'
