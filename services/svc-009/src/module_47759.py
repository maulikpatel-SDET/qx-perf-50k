"""Service module 47759: business logic, no crypto."""


def calculate_total_47759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47759():
    return 'module 47759 handles orders and invoices'
