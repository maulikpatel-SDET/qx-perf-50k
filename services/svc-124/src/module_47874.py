"""Service module 47874: business logic, no crypto."""


def calculate_total_47874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47874():
    return 'module 47874 handles orders and invoices'
