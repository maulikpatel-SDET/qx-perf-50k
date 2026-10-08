"""Service module 16041: business logic, no crypto."""


def calculate_total_16041(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16041():
    return 'module 16041 handles orders and invoices'
