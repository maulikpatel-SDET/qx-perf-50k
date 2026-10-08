"""Service module 5658: business logic, no crypto."""


def calculate_total_5658(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5658():
    return 'module 5658 handles orders and invoices'
