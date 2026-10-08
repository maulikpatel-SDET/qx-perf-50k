"""Service module 35696: business logic, no crypto."""


def calculate_total_35696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35696():
    return 'module 35696 handles orders and invoices'
