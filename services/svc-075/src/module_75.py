"""Service module 75: business logic, no crypto."""


def calculate_total_75(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_75():
    return 'module 75 handles orders and invoices'
