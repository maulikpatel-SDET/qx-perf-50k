"""Service module 33989: business logic, no crypto."""


def calculate_total_33989(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33989():
    return 'module 33989 handles orders and invoices'
