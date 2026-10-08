"""Service module 36653: business logic, no crypto."""


def calculate_total_36653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36653():
    return 'module 36653 handles orders and invoices'
