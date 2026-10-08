"""Service module 27937: business logic, no crypto."""


def calculate_total_27937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27937():
    return 'module 27937 handles orders and invoices'
