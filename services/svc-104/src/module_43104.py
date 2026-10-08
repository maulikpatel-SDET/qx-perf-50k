"""Service module 43104: business logic, no crypto."""


def calculate_total_43104(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43104():
    return 'module 43104 handles orders and invoices'
