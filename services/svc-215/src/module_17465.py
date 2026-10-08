"""Service module 17465: business logic, no crypto."""


def calculate_total_17465(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17465():
    return 'module 17465 handles orders and invoices'
