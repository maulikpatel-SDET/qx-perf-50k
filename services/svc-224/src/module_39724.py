"""Service module 39724: business logic, no crypto."""


def calculate_total_39724(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39724():
    return 'module 39724 handles orders and invoices'
