"""Service module 28759: business logic, no crypto."""


def calculate_total_28759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28759():
    return 'module 28759 handles orders and invoices'
