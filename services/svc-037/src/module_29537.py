"""Service module 29537: business logic, no crypto."""


def calculate_total_29537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29537():
    return 'module 29537 handles orders and invoices'
