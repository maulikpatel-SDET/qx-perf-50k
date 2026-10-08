"""Service module 25866: business logic, no crypto."""


def calculate_total_25866(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25866():
    return 'module 25866 handles orders and invoices'
