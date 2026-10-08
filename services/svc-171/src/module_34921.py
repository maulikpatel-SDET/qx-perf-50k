"""Service module 34921: business logic, no crypto."""


def calculate_total_34921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34921():
    return 'module 34921 handles orders and invoices'
