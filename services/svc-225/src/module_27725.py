"""Service module 27725: business logic, no crypto."""


def calculate_total_27725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27725():
    return 'module 27725 handles orders and invoices'
