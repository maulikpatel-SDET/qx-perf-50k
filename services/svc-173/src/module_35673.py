"""Service module 35673: business logic, no crypto."""


def calculate_total_35673(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35673():
    return 'module 35673 handles orders and invoices'
