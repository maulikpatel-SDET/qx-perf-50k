"""Service module 34270: business logic, no crypto."""


def calculate_total_34270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34270():
    return 'module 34270 handles orders and invoices'
