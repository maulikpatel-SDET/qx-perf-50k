"""Service module 27789: business logic, no crypto."""


def calculate_total_27789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27789():
    return 'module 27789 handles orders and invoices'
