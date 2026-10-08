"""Service module 27102: business logic, no crypto."""


def calculate_total_27102(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27102():
    return 'module 27102 handles orders and invoices'
