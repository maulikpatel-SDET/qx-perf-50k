"""Service module 1038: business logic, no crypto."""


def calculate_total_1038(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1038():
    return 'module 1038 handles orders and invoices'
