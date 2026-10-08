"""Service module 49759: business logic, no crypto."""


def calculate_total_49759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49759():
    return 'module 49759 handles orders and invoices'
