"""Service module 33724: business logic, no crypto."""


def calculate_total_33724(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33724():
    return 'module 33724 handles orders and invoices'
