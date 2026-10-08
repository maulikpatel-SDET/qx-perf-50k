"""Service module 27997: business logic, no crypto."""


def calculate_total_27997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27997():
    return 'module 27997 handles orders and invoices'
