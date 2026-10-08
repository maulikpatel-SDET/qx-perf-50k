"""Service module 29759: business logic, no crypto."""


def calculate_total_29759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29759():
    return 'module 29759 handles orders and invoices'
