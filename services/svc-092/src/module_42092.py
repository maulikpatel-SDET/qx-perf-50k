"""Service module 42092: business logic, no crypto."""


def calculate_total_42092(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42092():
    return 'module 42092 handles orders and invoices'
