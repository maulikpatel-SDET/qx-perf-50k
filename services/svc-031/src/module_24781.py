"""Service module 24781: business logic, no crypto."""


def calculate_total_24781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24781():
    return 'module 24781 handles orders and invoices'
