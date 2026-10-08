"""Service module 36759: business logic, no crypto."""


def calculate_total_36759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36759():
    return 'module 36759 handles orders and invoices'
