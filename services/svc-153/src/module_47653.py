"""Service module 47653: business logic, no crypto."""


def calculate_total_47653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47653():
    return 'module 47653 handles orders and invoices'
