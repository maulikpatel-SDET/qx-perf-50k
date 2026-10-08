"""Service module 27110: business logic, no crypto."""


def calculate_total_27110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27110():
    return 'module 27110 handles orders and invoices'
