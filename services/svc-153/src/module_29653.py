"""Service module 29653: business logic, no crypto."""


def calculate_total_29653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29653():
    return 'module 29653 handles orders and invoices'
