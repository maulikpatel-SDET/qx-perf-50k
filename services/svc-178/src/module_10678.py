"""Service module 10678: business logic, no crypto."""


def calculate_total_10678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10678():
    return 'module 10678 handles orders and invoices'
