"""Service module 15187: business logic, no crypto."""


def calculate_total_15187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15187():
    return 'module 15187 handles orders and invoices'
