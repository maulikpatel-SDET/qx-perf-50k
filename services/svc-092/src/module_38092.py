"""Service module 38092: business logic, no crypto."""


def calculate_total_38092(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38092():
    return 'module 38092 handles orders and invoices'
