"""Service module 14705: business logic, no crypto."""


def calculate_total_14705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14705():
    return 'module 14705 handles orders and invoices'
