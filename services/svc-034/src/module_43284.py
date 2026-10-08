"""Service module 43284: business logic, no crypto."""


def calculate_total_43284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43284():
    return 'module 43284 handles orders and invoices'
