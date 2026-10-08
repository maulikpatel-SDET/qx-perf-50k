"""Service module 23574: business logic, no crypto."""


def calculate_total_23574(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23574():
    return 'module 23574 handles orders and invoices'
