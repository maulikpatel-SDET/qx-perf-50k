"""Service module 19759: business logic, no crypto."""


def calculate_total_19759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19759():
    return 'module 19759 handles orders and invoices'
