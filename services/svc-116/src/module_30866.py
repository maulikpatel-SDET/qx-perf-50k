"""Service module 30866: business logic, no crypto."""


def calculate_total_30866(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30866():
    return 'module 30866 handles orders and invoices'
