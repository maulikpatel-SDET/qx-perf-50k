"""Service module 13092: business logic, no crypto."""


def calculate_total_13092(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13092():
    return 'module 13092 handles orders and invoices'
