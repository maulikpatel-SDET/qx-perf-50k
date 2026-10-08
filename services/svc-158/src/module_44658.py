"""Service module 44658: business logic, no crypto."""


def calculate_total_44658(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44658():
    return 'module 44658 handles orders and invoices'
