"""Service module 42898: business logic, no crypto."""


def calculate_total_42898(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42898():
    return 'module 42898 handles orders and invoices'
