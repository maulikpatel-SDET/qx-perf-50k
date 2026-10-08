"""Service module 18705: business logic, no crypto."""


def calculate_total_18705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18705():
    return 'module 18705 handles orders and invoices'
