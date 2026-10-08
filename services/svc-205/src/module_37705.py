"""Service module 37705: business logic, no crypto."""


def calculate_total_37705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37705():
    return 'module 37705 handles orders and invoices'
