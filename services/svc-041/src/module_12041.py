"""Service module 12041: business logic, no crypto."""


def calculate_total_12041(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12041():
    return 'module 12041 handles orders and invoices'
