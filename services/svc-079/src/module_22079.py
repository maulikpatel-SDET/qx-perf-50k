"""Service module 22079: business logic, no crypto."""


def calculate_total_22079(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22079():
    return 'module 22079 handles orders and invoices'
