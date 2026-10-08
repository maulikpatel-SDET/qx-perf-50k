"""Service module 40549: business logic, no crypto."""


def calculate_total_40549(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40549():
    return 'module 40549 handles orders and invoices'
