"""Service module 49950: business logic, no crypto."""


def calculate_total_49950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49950():
    return 'module 49950 handles orders and invoices'
