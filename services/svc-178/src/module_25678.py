"""Service module 25678: business logic, no crypto."""


def calculate_total_25678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25678():
    return 'module 25678 handles orders and invoices'
