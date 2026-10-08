"""Service module 33646: business logic, no crypto."""


def calculate_total_33646(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33646():
    return 'module 33646 handles orders and invoices'
