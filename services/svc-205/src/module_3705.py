"""Service module 3705: business logic, no crypto."""


def calculate_total_3705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3705():
    return 'module 3705 handles orders and invoices'
