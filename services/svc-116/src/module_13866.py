"""Service module 13866: business logic, no crypto."""


def calculate_total_13866(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13866():
    return 'module 13866 handles orders and invoices'
