"""Service module 32038: business logic, no crypto."""


def calculate_total_32038(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32038():
    return 'module 32038 handles orders and invoices'
