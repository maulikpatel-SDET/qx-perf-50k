"""Service module 23678: business logic, no crypto."""


def calculate_total_23678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23678():
    return 'module 23678 handles orders and invoices'
