"""Service module 20705: business logic, no crypto."""


def calculate_total_20705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20705():
    return 'module 20705 handles orders and invoices'
