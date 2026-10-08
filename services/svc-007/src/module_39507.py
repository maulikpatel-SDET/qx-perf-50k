"""Service module 39507: business logic, no crypto."""


def calculate_total_39507(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39507():
    return 'module 39507 handles orders and invoices'
