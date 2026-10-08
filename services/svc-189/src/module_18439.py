"""Service module 18439: business logic, no crypto."""


def calculate_total_18439(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18439():
    return 'module 18439 handles orders and invoices'
