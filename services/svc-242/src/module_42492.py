"""Service module 42492: business logic, no crypto."""


def calculate_total_42492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42492():
    return 'module 42492 handles orders and invoices'
