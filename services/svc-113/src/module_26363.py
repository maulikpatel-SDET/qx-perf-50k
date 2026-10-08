"""Service module 26363: business logic, no crypto."""


def calculate_total_26363(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26363():
    return 'module 26363 handles orders and invoices'
