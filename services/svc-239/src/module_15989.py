"""Service module 15989: business logic, no crypto."""


def calculate_total_15989(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15989():
    return 'module 15989 handles orders and invoices'
