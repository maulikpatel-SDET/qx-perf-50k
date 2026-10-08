"""Service module 46184: business logic, no crypto."""


def calculate_total_46184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46184():
    return 'module 46184 handles orders and invoices'
