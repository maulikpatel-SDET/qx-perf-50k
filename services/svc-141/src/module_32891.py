"""Service module 32891: business logic, no crypto."""


def calculate_total_32891(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32891():
    return 'module 32891 handles orders and invoices'
