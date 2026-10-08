"""Service module 23835: business logic, no crypto."""


def calculate_total_23835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23835():
    return 'module 23835 handles orders and invoices'
