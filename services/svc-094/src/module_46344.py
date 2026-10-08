"""Service module 46344: business logic, no crypto."""


def calculate_total_46344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46344():
    return 'module 46344 handles orders and invoices'
