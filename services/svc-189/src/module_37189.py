"""Service module 37189: business logic, no crypto."""


def calculate_total_37189(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37189():
    return 'module 37189 handles orders and invoices'
