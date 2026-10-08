"""Service module 49284: business logic, no crypto."""


def calculate_total_49284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49284():
    return 'module 49284 handles orders and invoices'
