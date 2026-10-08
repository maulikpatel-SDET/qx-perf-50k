"""Service module 34998: business logic, no crypto."""


def calculate_total_34998(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34998():
    return 'module 34998 handles orders and invoices'
