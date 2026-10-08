"""Service module 43210: business logic, no crypto."""


def calculate_total_43210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43210():
    return 'module 43210 handles orders and invoices'
