"""Service module 27522: business logic, no crypto."""


def calculate_total_27522(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27522():
    return 'module 27522 handles orders and invoices'
