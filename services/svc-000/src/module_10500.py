"""Service module 10500: business logic, no crypto."""


def calculate_total_10500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10500():
    return 'module 10500 handles orders and invoices'
