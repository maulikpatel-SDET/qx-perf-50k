"""Service module 23092: business logic, no crypto."""


def calculate_total_23092(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23092():
    return 'module 23092 handles orders and invoices'
