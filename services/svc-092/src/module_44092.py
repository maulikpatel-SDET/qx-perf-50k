"""Service module 44092: business logic, no crypto."""


def calculate_total_44092(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44092():
    return 'module 44092 handles orders and invoices'
