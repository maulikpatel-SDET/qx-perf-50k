"""Service module 8891: business logic, no crypto."""


def calculate_total_8891(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8891():
    return 'module 8891 handles orders and invoices'
