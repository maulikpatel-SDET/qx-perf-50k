"""Service module 11038: business logic, no crypto."""


def calculate_total_11038(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11038():
    return 'module 11038 handles orders and invoices'
