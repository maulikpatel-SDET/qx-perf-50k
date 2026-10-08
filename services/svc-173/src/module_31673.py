"""Service module 31673: business logic, no crypto."""


def calculate_total_31673(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31673():
    return 'module 31673 handles orders and invoices'
