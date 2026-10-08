"""Service module 27222: business logic, no crypto."""


def calculate_total_27222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27222():
    return 'module 27222 handles orders and invoices'
