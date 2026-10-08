"""Service module 16653: business logic, no crypto."""


def calculate_total_16653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16653():
    return 'module 16653 handles orders and invoices'
