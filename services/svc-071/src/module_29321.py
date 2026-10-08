"""Service module 29321: business logic, no crypto."""


def calculate_total_29321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29321():
    return 'module 29321 handles orders and invoices'
