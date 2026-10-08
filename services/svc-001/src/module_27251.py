"""Service module 27251: business logic, no crypto."""


def calculate_total_27251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27251():
    return 'module 27251 handles orders and invoices'
