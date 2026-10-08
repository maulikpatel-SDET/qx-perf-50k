"""Service module 45933: business logic, no crypto."""


def calculate_total_45933(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45933():
    return 'module 45933 handles orders and invoices'
