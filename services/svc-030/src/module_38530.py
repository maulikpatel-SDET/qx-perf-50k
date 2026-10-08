"""Service module 38530: business logic, no crypto."""


def calculate_total_38530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38530():
    return 'module 38530 handles orders and invoices'
