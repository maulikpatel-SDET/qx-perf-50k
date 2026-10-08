"""Service module 13748: business logic, no crypto."""


def calculate_total_13748(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13748():
    return 'module 13748 handles orders and invoices'
