"""Service module 44189: business logic, no crypto."""


def calculate_total_44189(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44189():
    return 'module 44189 handles orders and invoices'
