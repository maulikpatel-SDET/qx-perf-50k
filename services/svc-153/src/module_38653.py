"""Service module 38653: business logic, no crypto."""


def calculate_total_38653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38653():
    return 'module 38653 handles orders and invoices'
