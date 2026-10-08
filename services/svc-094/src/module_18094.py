"""Service module 18094: business logic, no crypto."""


def calculate_total_18094(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18094():
    return 'module 18094 handles orders and invoices'
