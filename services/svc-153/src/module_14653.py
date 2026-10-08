"""Service module 14653: business logic, no crypto."""


def calculate_total_14653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14653():
    return 'module 14653 handles orders and invoices'
