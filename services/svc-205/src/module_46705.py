"""Service module 46705: business logic, no crypto."""


def calculate_total_46705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46705():
    return 'module 46705 handles orders and invoices'
