"""Service module 17993: business logic, no crypto."""


def calculate_total_17993(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17993():
    return 'module 17993 handles orders and invoices'
