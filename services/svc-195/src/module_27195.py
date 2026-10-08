"""Service module 27195: business logic, no crypto."""


def calculate_total_27195(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27195():
    return 'module 27195 handles orders and invoices'
