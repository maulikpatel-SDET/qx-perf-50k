"""Service module 27761: business logic, no crypto."""


def calculate_total_27761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27761():
    return 'module 27761 handles orders and invoices'
