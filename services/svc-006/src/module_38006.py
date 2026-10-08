"""Service module 38006: business logic, no crypto."""


def calculate_total_38006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38006():
    return 'module 38006 handles orders and invoices'
