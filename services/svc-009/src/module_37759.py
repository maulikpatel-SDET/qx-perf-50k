"""Service module 37759: business logic, no crypto."""


def calculate_total_37759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37759():
    return 'module 37759 handles orders and invoices'
