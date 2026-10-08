"""Service module 8653: business logic, no crypto."""


def calculate_total_8653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8653():
    return 'module 8653 handles orders and invoices'
