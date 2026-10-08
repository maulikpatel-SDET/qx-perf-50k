"""Service module 43256: business logic, no crypto."""


def calculate_total_43256(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43256():
    return 'module 43256 handles orders and invoices'
