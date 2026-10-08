"""Service module 3748: business logic, no crypto."""


def calculate_total_3748(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3748():
    return 'module 3748 handles orders and invoices'
