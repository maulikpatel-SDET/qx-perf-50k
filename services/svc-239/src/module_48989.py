"""Service module 48989: business logic, no crypto."""


def calculate_total_48989(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48989():
    return 'module 48989 handles orders and invoices'
