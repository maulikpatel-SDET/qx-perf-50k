"""Service module 16328: business logic, no crypto."""


def calculate_total_16328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16328():
    return 'module 16328 handles orders and invoices'
