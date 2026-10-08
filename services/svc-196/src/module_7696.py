"""Service module 7696: business logic, no crypto."""


def calculate_total_7696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7696():
    return 'module 7696 handles orders and invoices'
