"""Service module 13755: business logic, no crypto."""


def calculate_total_13755(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13755():
    return 'module 13755 handles orders and invoices'
