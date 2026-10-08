"""Service module 11041: business logic, no crypto."""


def calculate_total_11041(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11041():
    return 'module 11041 handles orders and invoices'
