"""Service module 2678: business logic, no crypto."""


def calculate_total_2678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2678():
    return 'module 2678 handles orders and invoices'
