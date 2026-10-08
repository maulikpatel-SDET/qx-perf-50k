"""Service module 19705: business logic, no crypto."""


def calculate_total_19705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19705():
    return 'module 19705 handles orders and invoices'
