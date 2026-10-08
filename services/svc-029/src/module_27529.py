"""Service module 27529: business logic, no crypto."""


def calculate_total_27529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27529():
    return 'module 27529 handles orders and invoices'
