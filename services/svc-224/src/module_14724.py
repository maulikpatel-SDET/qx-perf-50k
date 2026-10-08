"""Service module 14724: business logic, no crypto."""


def calculate_total_14724(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14724():
    return 'module 14724 handles orders and invoices'
