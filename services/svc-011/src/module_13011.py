"""Service module 13011: business logic, no crypto."""


def calculate_total_13011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13011():
    return 'module 13011 handles orders and invoices'
