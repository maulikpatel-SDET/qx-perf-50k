"""Service module 35705: business logic, no crypto."""


def calculate_total_35705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35705():
    return 'module 35705 handles orders and invoices'
