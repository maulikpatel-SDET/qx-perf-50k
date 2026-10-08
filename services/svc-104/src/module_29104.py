"""Service module 29104: business logic, no crypto."""


def calculate_total_29104(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29104():
    return 'module 29104 handles orders and invoices'
