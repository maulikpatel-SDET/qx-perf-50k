"""Service module 48658: business logic, no crypto."""


def calculate_total_48658(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48658():
    return 'module 48658 handles orders and invoices'
