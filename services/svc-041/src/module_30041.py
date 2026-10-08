"""Service module 30041: business logic, no crypto."""


def calculate_total_30041(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30041():
    return 'module 30041 handles orders and invoices'
