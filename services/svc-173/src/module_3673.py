"""Service module 3673: business logic, no crypto."""


def calculate_total_3673(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3673():
    return 'module 3673 handles orders and invoices'
