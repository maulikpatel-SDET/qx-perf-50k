"""Service module 43485: business logic, no crypto."""


def calculate_total_43485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43485():
    return 'module 43485 handles orders and invoices'
