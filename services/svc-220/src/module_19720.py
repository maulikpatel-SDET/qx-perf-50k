"""Service module 19720: business logic, no crypto."""


def calculate_total_19720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19720():
    return 'module 19720 handles orders and invoices'
