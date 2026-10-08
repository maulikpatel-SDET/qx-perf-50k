"""Service module 48910: business logic, no crypto."""


def calculate_total_48910(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48910():
    return 'module 48910 handles orders and invoices'
