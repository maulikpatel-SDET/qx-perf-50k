"""Service module 39866: business logic, no crypto."""


def calculate_total_39866(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39866():
    return 'module 39866 handles orders and invoices'
