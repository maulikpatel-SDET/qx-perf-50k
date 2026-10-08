"""Service module 30500: business logic, no crypto."""


def calculate_total_30500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30500():
    return 'module 30500 handles orders and invoices'
