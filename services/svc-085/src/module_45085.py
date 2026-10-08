"""Service module 45085: business logic, no crypto."""


def calculate_total_45085(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45085():
    return 'module 45085 handles orders and invoices'
