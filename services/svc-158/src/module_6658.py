"""Service module 6658: business logic, no crypto."""


def calculate_total_6658(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6658():
    return 'module 6658 handles orders and invoices'
