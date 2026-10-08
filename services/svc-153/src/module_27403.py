"""Service module 27403: business logic, no crypto."""


def calculate_total_27403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27403():
    return 'module 27403 handles orders and invoices'
