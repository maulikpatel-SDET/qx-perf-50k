"""Service module 45856: business logic, no crypto."""


def calculate_total_45856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45856():
    return 'module 45856 handles orders and invoices'
