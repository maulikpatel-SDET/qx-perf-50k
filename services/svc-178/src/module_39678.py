"""Service module 39678: business logic, no crypto."""


def calculate_total_39678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39678():
    return 'module 39678 handles orders and invoices'
