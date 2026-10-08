"""Service module 44705: business logic, no crypto."""


def calculate_total_44705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44705():
    return 'module 44705 handles orders and invoices'
