"""Service module 19856: business logic, no crypto."""


def calculate_total_19856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19856():
    return 'module 19856 handles orders and invoices'
