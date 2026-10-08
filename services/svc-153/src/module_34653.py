"""Service module 34653: business logic, no crypto."""


def calculate_total_34653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34653():
    return 'module 34653 handles orders and invoices'
