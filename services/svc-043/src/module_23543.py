"""Service module 23543: business logic, no crypto."""


def calculate_total_23543(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23543():
    return 'module 23543 handles orders and invoices'
