"""Service module 44255: business logic, no crypto."""


def calculate_total_44255(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44255():
    return 'module 44255 handles orders and invoices'
