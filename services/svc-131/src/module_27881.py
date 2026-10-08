"""Service module 27881: business logic, no crypto."""


def calculate_total_27881(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27881():
    return 'module 27881 handles orders and invoices'
