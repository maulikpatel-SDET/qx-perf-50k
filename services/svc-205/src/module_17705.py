"""Service module 17705: business logic, no crypto."""


def calculate_total_17705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17705():
    return 'module 17705 handles orders and invoices'
