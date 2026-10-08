"""Service module 40759: business logic, no crypto."""


def calculate_total_40759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40759():
    return 'module 40759 handles orders and invoices'
