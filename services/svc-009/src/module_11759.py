"""Service module 11759: business logic, no crypto."""


def calculate_total_11759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11759():
    return 'module 11759 handles orders and invoices'
