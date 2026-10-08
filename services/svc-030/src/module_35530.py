"""Service module 35530: business logic, no crypto."""


def calculate_total_35530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35530():
    return 'module 35530 handles orders and invoices'
