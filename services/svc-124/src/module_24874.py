"""Service module 24874: business logic, no crypto."""


def calculate_total_24874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24874():
    return 'module 24874 handles orders and invoices'
