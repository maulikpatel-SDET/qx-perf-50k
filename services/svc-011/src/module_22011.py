"""Service module 22011: business logic, no crypto."""


def calculate_total_22011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22011():
    return 'module 22011 handles orders and invoices'
