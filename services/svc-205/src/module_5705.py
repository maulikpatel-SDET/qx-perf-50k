"""Service module 5705: business logic, no crypto."""


def calculate_total_5705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5705():
    return 'module 5705 handles orders and invoices'
