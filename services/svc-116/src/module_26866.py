"""Service module 26866: business logic, no crypto."""


def calculate_total_26866(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26866():
    return 'module 26866 handles orders and invoices'
