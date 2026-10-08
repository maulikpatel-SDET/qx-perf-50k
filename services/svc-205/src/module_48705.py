"""Service module 48705: business logic, no crypto."""


def calculate_total_48705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48705():
    return 'module 48705 handles orders and invoices'
