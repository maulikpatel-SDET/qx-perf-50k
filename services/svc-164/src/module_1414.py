"""Service module 1414: business logic, no crypto."""


def calculate_total_1414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1414():
    return 'module 1414 handles orders and invoices'
