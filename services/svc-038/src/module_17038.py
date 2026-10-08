"""Service module 17038: business logic, no crypto."""


def calculate_total_17038(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17038():
    return 'module 17038 handles orders and invoices'
