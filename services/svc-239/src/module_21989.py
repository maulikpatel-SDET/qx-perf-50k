"""Service module 21989: business logic, no crypto."""


def calculate_total_21989(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21989():
    return 'module 21989 handles orders and invoices'
