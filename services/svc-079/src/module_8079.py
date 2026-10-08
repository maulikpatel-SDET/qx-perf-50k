"""Service module 8079: business logic, no crypto."""


def calculate_total_8079(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8079():
    return 'module 8079 handles orders and invoices'
