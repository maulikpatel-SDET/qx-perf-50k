"""Service module 30989: business logic, no crypto."""


def calculate_total_30989(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30989():
    return 'module 30989 handles orders and invoices'
