"""Service module 19431: business logic, no crypto."""


def calculate_total_19431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19431():
    return 'module 19431 handles orders and invoices'
