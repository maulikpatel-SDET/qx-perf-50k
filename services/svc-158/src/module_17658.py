"""Service module 17658: business logic, no crypto."""


def calculate_total_17658(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17658():
    return 'module 17658 handles orders and invoices'
