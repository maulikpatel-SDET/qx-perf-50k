"""Service module 35503: business logic, no crypto."""


def calculate_total_35503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35503():
    return 'module 35503 handles orders and invoices'
