"""Service module 36866: business logic, no crypto."""


def calculate_total_36866(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36866():
    return 'module 36866 handles orders and invoices'
