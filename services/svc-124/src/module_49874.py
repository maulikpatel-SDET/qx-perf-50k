"""Service module 49874: business logic, no crypto."""


def calculate_total_49874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49874():
    return 'module 49874 handles orders and invoices'
