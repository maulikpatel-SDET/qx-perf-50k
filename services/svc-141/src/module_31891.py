"""Service module 31891: business logic, no crypto."""


def calculate_total_31891(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31891():
    return 'module 31891 handles orders and invoices'
