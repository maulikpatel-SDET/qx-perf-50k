"""Service module 28218: business logic, no crypto."""


def calculate_total_28218(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28218():
    return 'module 28218 handles orders and invoices'
