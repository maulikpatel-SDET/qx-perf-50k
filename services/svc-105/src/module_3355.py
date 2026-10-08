"""Service module 3355: business logic, no crypto."""


def calculate_total_3355(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3355():
    return 'module 3355 handles orders and invoices'
