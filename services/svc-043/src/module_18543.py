"""Service module 18543: business logic, no crypto."""


def calculate_total_18543(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18543():
    return 'module 18543 handles orders and invoices'
