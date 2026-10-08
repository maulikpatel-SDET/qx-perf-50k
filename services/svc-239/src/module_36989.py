"""Service module 36989: business logic, no crypto."""


def calculate_total_36989(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36989():
    return 'module 36989 handles orders and invoices'
