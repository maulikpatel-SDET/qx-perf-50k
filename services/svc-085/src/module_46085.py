"""Service module 46085: business logic, no crypto."""


def calculate_total_46085(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46085():
    return 'module 46085 handles orders and invoices'
