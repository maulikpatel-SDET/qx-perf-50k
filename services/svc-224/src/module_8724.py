"""Service module 8724: business logic, no crypto."""


def calculate_total_8724(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8724():
    return 'module 8724 handles orders and invoices'
