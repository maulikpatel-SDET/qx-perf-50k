"""Service module 12759: business logic, no crypto."""


def calculate_total_12759(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12759():
    return 'module 12759 handles orders and invoices'
