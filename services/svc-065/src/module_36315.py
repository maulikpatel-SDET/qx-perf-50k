"""Service module 36315: business logic, no crypto."""


def calculate_total_36315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36315():
    return 'module 36315 handles orders and invoices'
