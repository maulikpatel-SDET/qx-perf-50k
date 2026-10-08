"""Service module 42998: business logic, no crypto."""


def calculate_total_42998(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42998():
    return 'module 42998 handles orders and invoices'
