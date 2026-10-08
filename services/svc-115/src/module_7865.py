"""Service module 7865: business logic, no crypto."""


def calculate_total_7865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7865():
    return 'module 7865 handles orders and invoices'
