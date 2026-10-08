"""Service module 24011: business logic, no crypto."""


def calculate_total_24011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24011():
    return 'module 24011 handles orders and invoices'
