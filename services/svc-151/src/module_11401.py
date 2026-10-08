"""Service module 11401: business logic, no crypto."""


def calculate_total_11401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11401():
    return 'module 11401 handles orders and invoices'
