"""Service module 43974: business logic, no crypto."""


def calculate_total_43974(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43974():
    return 'module 43974 handles orders and invoices'
