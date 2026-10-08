"""Service module 17128: business logic, no crypto."""


def calculate_total_17128(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17128():
    return 'module 17128 handles orders and invoices'
