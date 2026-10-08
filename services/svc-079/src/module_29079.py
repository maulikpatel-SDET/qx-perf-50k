"""Service module 29079: business logic, no crypto."""


def calculate_total_29079(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29079():
    return 'module 29079 handles orders and invoices'
