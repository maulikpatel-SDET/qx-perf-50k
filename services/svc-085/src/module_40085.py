"""Service module 40085: business logic, no crypto."""


def calculate_total_40085(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40085():
    return 'module 40085 handles orders and invoices'
