"""Service module 27118: business logic, no crypto."""


def calculate_total_27118(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27118():
    return 'module 27118 handles orders and invoices'
