"""Service module 29485: business logic, no crypto."""


def calculate_total_29485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29485():
    return 'module 29485 handles orders and invoices'
