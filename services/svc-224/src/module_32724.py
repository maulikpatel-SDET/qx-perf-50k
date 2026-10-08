"""Service module 32724: business logic, no crypto."""


def calculate_total_32724(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32724():
    return 'module 32724 handles orders and invoices'
