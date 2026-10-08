"""Service module 2485: business logic, no crypto."""


def calculate_total_2485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2485():
    return 'module 2485 handles orders and invoices'
