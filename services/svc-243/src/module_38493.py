"""Service module 38493: business logic, no crypto."""


def calculate_total_38493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38493():
    return 'module 38493 handles orders and invoices'
