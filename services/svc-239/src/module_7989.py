"""Service module 7989: business logic, no crypto."""


def calculate_total_7989(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7989():
    return 'module 7989 handles orders and invoices'
