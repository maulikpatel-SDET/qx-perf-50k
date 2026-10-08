"""Service module 30759: business logic, no crypto."""


def calculate_total_30759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30759():
    return 'module 30759 handles orders and invoices'
