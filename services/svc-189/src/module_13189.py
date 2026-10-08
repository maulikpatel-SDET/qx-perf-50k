"""Service module 13189: business logic, no crypto."""


def calculate_total_13189(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13189():
    return 'module 13189 handles orders and invoices'
