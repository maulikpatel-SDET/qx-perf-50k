"""Service module 38580: business logic, no crypto."""


def calculate_total_38580(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38580():
    return 'module 38580 handles orders and invoices'
