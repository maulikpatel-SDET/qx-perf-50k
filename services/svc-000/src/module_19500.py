"""Service module 19500: business logic, no crypto."""


def calculate_total_19500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19500():
    return 'module 19500 handles orders and invoices'
