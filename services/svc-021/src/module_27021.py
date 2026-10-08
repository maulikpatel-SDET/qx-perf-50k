"""Service module 27021: business logic, no crypto."""


def calculate_total_27021(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27021():
    return 'module 27021 handles orders and invoices'
