"""Service module 33104: business logic, no crypto."""


def calculate_total_33104(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33104():
    return 'module 33104 handles orders and invoices'
