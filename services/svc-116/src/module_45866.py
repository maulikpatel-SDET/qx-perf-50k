"""Service module 45866: business logic, no crypto."""


def calculate_total_45866(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45866():
    return 'module 45866 handles orders and invoices'
