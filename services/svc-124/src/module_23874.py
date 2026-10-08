"""Service module 23874: business logic, no crypto."""


def calculate_total_23874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23874():
    return 'module 23874 handles orders and invoices'
