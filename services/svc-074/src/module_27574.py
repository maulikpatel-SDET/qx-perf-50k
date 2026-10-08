"""Service module 27574: business logic, no crypto."""


def calculate_total_27574(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27574():
    return 'module 27574 handles orders and invoices'
