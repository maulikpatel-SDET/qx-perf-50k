"""Service module 27720: business logic, no crypto."""


def calculate_total_27720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27720():
    return 'module 27720 handles orders and invoices'
