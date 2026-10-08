"""Service module 25856: business logic, no crypto."""


def calculate_total_25856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25856():
    return 'module 25856 handles orders and invoices'
