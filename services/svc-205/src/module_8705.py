"""Service module 8705: business logic, no crypto."""


def calculate_total_8705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8705():
    return 'module 8705 handles orders and invoices'
