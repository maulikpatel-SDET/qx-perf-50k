"""Service module 34874: business logic, no crypto."""


def calculate_total_34874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34874():
    return 'module 34874 handles orders and invoices'
