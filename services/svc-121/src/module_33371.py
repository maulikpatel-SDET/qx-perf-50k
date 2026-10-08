"""Service module 33371: business logic, no crypto."""


def calculate_total_33371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33371():
    return 'module 33371 handles orders and invoices'
