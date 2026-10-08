"""Service module 11993: business logic, no crypto."""


def calculate_total_11993(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11993():
    return 'module 11993 handles orders and invoices'
