"""Service module 3721: business logic, no crypto."""


def calculate_total_3721(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3721():
    return 'module 3721 handles orders and invoices'
