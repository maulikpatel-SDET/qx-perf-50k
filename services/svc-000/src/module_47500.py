"""Service module 47500: business logic, no crypto."""


def calculate_total_47500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47500():
    return 'module 47500 handles orders and invoices'
