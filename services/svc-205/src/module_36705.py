"""Service module 36705: business logic, no crypto."""


def calculate_total_36705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36705():
    return 'module 36705 handles orders and invoices'
