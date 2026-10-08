"""Service module 18759: business logic, no crypto."""


def calculate_total_18759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18759():
    return 'module 18759 handles orders and invoices'
