"""Service module 27781: business logic, no crypto."""


def calculate_total_27781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27781():
    return 'module 27781 handles orders and invoices'
