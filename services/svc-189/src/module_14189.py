"""Service module 14189: business logic, no crypto."""


def calculate_total_14189(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14189():
    return 'module 14189 handles orders and invoices'
