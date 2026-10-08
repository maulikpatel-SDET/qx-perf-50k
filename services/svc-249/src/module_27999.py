"""Service module 27999: business logic, no crypto."""


def calculate_total_27999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27999():
    return 'module 27999 handles orders and invoices'
