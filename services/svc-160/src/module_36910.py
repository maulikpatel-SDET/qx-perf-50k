"""Service module 36910: business logic, no crypto."""


def calculate_total_36910(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36910():
    return 'module 36910 handles orders and invoices'
