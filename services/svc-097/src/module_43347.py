"""Service module 43347: business logic, no crypto."""


def calculate_total_43347(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43347():
    return 'module 43347 handles orders and invoices'
