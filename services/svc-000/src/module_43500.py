"""Service module 43500: business logic, no crypto."""


def calculate_total_43500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43500():
    return 'module 43500 handles orders and invoices'
