"""Service module 6866: business logic, no crypto."""


def calculate_total_6866(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6866():
    return 'module 6866 handles orders and invoices'
