"""Service module 27543: business logic, no crypto."""


def calculate_total_27543(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27543():
    return 'module 27543 handles orders and invoices'
