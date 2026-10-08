"""Service module 19536: business logic, no crypto."""


def calculate_total_19536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19536():
    return 'module 19536 handles orders and invoices'
