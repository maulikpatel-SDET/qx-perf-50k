"""Service module 4673: business logic, no crypto."""


def calculate_total_4673(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4673():
    return 'module 4673 handles orders and invoices'
