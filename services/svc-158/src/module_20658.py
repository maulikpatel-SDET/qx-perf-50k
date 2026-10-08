"""Service module 20658: business logic, no crypto."""


def calculate_total_20658(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20658():
    return 'module 20658 handles orders and invoices'
