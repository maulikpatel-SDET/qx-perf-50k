"""Service module 17891: business logic, no crypto."""


def calculate_total_17891(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17891():
    return 'module 17891 handles orders and invoices'
