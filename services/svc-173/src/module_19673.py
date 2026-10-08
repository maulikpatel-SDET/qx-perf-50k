"""Service module 19673: business logic, no crypto."""


def calculate_total_19673(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19673():
    return 'module 19673 handles orders and invoices'
