"""Service module 7442: business logic, no crypto."""


def calculate_total_7442(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7442():
    return 'module 7442 handles orders and invoices'
