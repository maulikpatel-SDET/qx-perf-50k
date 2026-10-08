"""Service module 45720: business logic, no crypto."""


def calculate_total_45720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45720():
    return 'module 45720 handles orders and invoices'
