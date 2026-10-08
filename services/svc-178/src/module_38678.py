"""Service module 38678: business logic, no crypto."""


def calculate_total_38678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38678():
    return 'module 38678 handles orders and invoices'
