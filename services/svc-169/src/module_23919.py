"""Service module 23919: business logic, no crypto."""


def calculate_total_23919(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23919():
    return 'module 23919 handles orders and invoices'
