"""Service module 25092: business logic, no crypto."""


def calculate_total_25092(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25092():
    return 'module 25092 handles orders and invoices'
