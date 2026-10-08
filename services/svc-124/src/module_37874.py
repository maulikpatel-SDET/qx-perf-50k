"""Service module 37874: business logic, no crypto."""


def calculate_total_37874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37874():
    return 'module 37874 handles orders and invoices'
