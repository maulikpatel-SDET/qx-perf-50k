"""Service module 27033: business logic, no crypto."""


def calculate_total_27033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27033():
    return 'module 27033 handles orders and invoices'
