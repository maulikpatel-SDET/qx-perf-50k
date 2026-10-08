"""Service module 31094: business logic, no crypto."""


def calculate_total_31094(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31094():
    return 'module 31094 handles orders and invoices'
