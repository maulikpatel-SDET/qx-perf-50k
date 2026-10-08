"""Service module 39658: business logic, no crypto."""


def calculate_total_39658(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39658():
    return 'module 39658 handles orders and invoices'
