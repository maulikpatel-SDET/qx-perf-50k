"""Service module 21730: business logic, no crypto."""


def calculate_total_21730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21730():
    return 'module 21730 handles orders and invoices'
