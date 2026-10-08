"""Service module 46673: business logic, no crypto."""


def calculate_total_46673(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46673():
    return 'module 46673 handles orders and invoices'
