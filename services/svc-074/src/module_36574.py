"""Service module 36574: business logic, no crypto."""


def calculate_total_36574(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36574():
    return 'module 36574 handles orders and invoices'
