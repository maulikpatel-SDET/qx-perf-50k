"""Service module 4574: business logic, no crypto."""


def calculate_total_4574(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4574():
    return 'module 4574 handles orders and invoices'
