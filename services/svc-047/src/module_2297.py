"""Service module 2297: business logic, no crypto."""


def calculate_total_2297(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2297():
    return 'module 2297 handles orders and invoices'
