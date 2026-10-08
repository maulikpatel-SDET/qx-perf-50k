"""Service module 35195: business logic, no crypto."""


def calculate_total_35195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35195():
    return 'module 35195 handles orders and invoices'
