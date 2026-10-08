"""Service module 29213: business logic, no crypto."""


def calculate_total_29213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29213():
    return 'module 29213 handles orders and invoices'
