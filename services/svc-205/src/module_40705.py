"""Service module 40705: business logic, no crypto."""


def calculate_total_40705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40705():
    return 'module 40705 handles orders and invoices'
