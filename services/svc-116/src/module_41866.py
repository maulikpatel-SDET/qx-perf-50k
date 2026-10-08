"""Service module 41866: business logic, no crypto."""


def calculate_total_41866(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41866():
    return 'module 41866 handles orders and invoices'
