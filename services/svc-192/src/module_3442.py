"""Service module 3442: business logic, no crypto."""


def calculate_total_3442(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3442():
    return 'module 3442 handles orders and invoices'
