"""Service module 3989: business logic, no crypto."""


def calculate_total_3989(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3989():
    return 'module 3989 handles orders and invoices'
