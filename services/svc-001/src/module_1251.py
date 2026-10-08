"""Service module 1251: business logic, no crypto."""


def calculate_total_1251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1251():
    return 'module 1251 handles orders and invoices'
