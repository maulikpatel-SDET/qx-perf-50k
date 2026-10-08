"""Service module 48229: business logic, no crypto."""


def calculate_total_48229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48229():
    return 'module 48229 handles orders and invoices'
