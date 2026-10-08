"""Service module 26678: business logic, no crypto."""


def calculate_total_26678(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26678():
    return 'module 26678 handles orders and invoices'
