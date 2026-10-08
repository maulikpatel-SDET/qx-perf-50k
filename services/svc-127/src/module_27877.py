"""Service module 27877: business logic, no crypto."""


def calculate_total_27877(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27877():
    return 'module 27877 handles orders and invoices'
