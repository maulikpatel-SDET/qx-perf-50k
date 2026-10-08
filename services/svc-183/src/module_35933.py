"""Service module 35933: business logic, no crypto."""


def calculate_total_35933(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35933():
    return 'module 35933 handles orders and invoices'
