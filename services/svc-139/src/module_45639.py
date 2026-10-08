"""Service module 45639: business logic, no crypto."""


def calculate_total_45639(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45639():
    return 'module 45639 handles orders and invoices'
