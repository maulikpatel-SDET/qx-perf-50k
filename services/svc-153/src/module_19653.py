"""Service module 19653: business logic, no crypto."""


def calculate_total_19653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19653():
    return 'module 19653 handles orders and invoices'
