"""Service module 28705: business logic, no crypto."""


def calculate_total_28705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28705():
    return 'module 28705 handles orders and invoices'
