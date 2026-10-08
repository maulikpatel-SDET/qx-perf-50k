"""Service module 27145: business logic, no crypto."""


def calculate_total_27145(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27145():
    return 'module 27145 handles orders and invoices'
