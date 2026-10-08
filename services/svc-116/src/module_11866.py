"""Service module 11866: business logic, no crypto."""


def calculate_total_11866(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11866():
    return 'module 11866 handles orders and invoices'
