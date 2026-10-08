"""Service module 678: business logic, no crypto."""


def calculate_total_678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_678():
    return 'module 678 handles orders and invoices'
