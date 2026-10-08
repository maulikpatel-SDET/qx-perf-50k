"""Service module 31705: business logic, no crypto."""


def calculate_total_31705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31705():
    return 'module 31705 handles orders and invoices'
