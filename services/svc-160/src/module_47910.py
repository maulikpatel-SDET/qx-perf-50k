"""Service module 47910: business logic, no crypto."""


def calculate_total_47910(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47910():
    return 'module 47910 handles orders and invoices'
