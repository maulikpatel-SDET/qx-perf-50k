"""Service module 21653: business logic, no crypto."""


def calculate_total_21653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21653():
    return 'module 21653 handles orders and invoices'
