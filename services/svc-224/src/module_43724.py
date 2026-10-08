"""Service module 43724: business logic, no crypto."""


def calculate_total_43724(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43724():
    return 'module 43724 handles orders and invoices'
