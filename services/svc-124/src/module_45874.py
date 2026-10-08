"""Service module 45874: business logic, no crypto."""


def calculate_total_45874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45874():
    return 'module 45874 handles orders and invoices'
